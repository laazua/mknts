package v2ray

import (
	"context"
	"log"
	"v2man/pkg/config"
	"v2man/storage"
	"v2man/storage/model"

	"github.com/google/uuid"
	pb "github.com/v2fly/v2ray-core/v5/app/stats/command" // 导入 V2Ray stats RPC 的包
	"google.golang.org/grpc"
)

const (
	Traffic20  int64 = 20 * 1024 * 1024  // 20G
	Traffic50  int64 = 50 * 1024 * 1024  // 50G
	Traffic120 int64 = 120 * 1024 * 1024 // 120G
)

// 定义流量限制的映射
var TrafficLimits = map[string]int64{
	"m20":  Traffic20,
	"m50":  Traffic50,
	"m120": Traffic120,
}

type UserTraffic struct {
	conn      *grpc.ClientConn
	client    pb.StatsServiceClient
	dbHandler *storage.DbHandler
}

func NewUserTraffic(cfg *config.Config, dbhandler *storage.DbHandler) *UserTraffic {
	conn, err := grpc.Dial(cfg.V2Address, grpc.WithInsecure())
	if err != nil {
		return nil
	}

	client := pb.NewStatsServiceClient(conn)
	return &UserTraffic{conn: conn, client: client, dbHandler: dbhandler}
}

func (u *UserTraffic) Close() {
	u.conn.Close()
}

func (u *UserTraffic) QueryUser() ([]model.User, error) {
	var users []model.User
	if err := u.dbHandler.DB.Find(&users).Error; err != nil {
		return nil, err
	}
	return users, nil
}

func (u *UserTraffic) UpdateUser(user model.User) error {
	return u.dbHandler.DB.Save(user).Error
}

func (u *UserTraffic) UpdateUserTraffic() {
	users, err := u.QueryUser()
	if err != nil || users == nil {
		log.Fatalf("Query User Error: %v\n", err)
		return
	}
	for _, user := range users {
		upLinkReq := &pb.QueryStatsRequest{
			Reset_:  true,
			Regexp:  true,
			Pattern: user.Name + ".+uplink",
		}
		downLinkReq := &pb.QueryStatsRequest{
			Reset_:  true,
			Regexp:  true,
			Pattern: user.Name + ".+downlink",
		}
		upLinkResp, err := u.client.QueryStats(context.Background(), upLinkReq)
		if err != nil {
			log.Fatalf("v2ray api stats uplink error: %v\n", err)
			return
		}
		downLinkResp, err := u.client.QueryStats(context.Background(), downLinkReq)
		if err != nil {
			log.Fatalf("v2ray api stats downlink error: %v\n", err)
			return
		}
		user.TrafficUp += upLinkResp.Stat[0].Value     // KB
		user.TrafficDown += downLinkResp.Stat[0].Value // KB
		// 检查流量标签并更新 UUID
		if limit, exists := TrafficLimits[user.TrafficTag]; exists && (user.TrafficUp+user.TrafficDown) > limit {
			user.Uuid = uuid.New()
		}
		log.Printf("更新用户: %s, 上行流量: %vKB, 下行流量: %vKB\n", user.Name, user.TrafficUp, user.TrafficDown)
		u.UpdateUser(user)
	}
}
