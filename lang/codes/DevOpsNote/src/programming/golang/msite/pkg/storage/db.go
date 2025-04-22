package storage

import (
	_ "github.com/lib/pq" // 导入 PostgreSQL 驱动
)

// var db *sql.DB

// func LoadSql() {
// 	pool, err := sql.Open("postgres", os.Getenv("storage.db.uri"))
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer pool.Close()

// 	pool.SetConnMaxLifetime(env.ParseTDuration(os.Getenv("storage.db.conn.lifetime"))) // <= not close
// 	pool.SetMaxIdleConns(env.StoInt(os.Getenv("storage.db.conn.max.idle")))
// 	pool.SetMaxOpenConns(env.StoInt(os.Getenv("storage.db.conn.max.open")))

// 	ctx, stop := context.WithCancel(context.Background())
// 	defer stop()

// 	appSignal := make(chan os.Signal, 3)
// 	signal.Notify(appSignal, os.Interrupt)

// 	go func() {
// 		<-appSignal
// 		stop()
// 	}()

// 	db = pool

// 	ping(ctx)

// 	query(ctx, 10)
// }

// func ping(ctx context.Context) {
// 	ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
// 	defer cancel()

// 	if err := db.PingContext(ctx); err != nil {
// 		log.Fatalf("unable to connect to database: %v", err)
// 	}
// }

// 数据库查询示例
// func query(ctx context.Context, id int64) {
// 	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
// 	defer cancel()

// 	var name string
// 	err := DB.QueryRowContext(ctx, "select p.name from people as p where p.id = :id;", sql.Named("id", id)).Scan(&name)
// 	if err != nil {
// 		log.Fatal("unable to execute search query", err)
// 	}
// 	log.Println("name=", name)
// }
