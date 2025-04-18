package dto

import "gweb/pkg/utils"

func AddZoneToDb(name, ip string, id int) bool {
	sql := `
	  INSERT INTO zone(ZoneName, ZoneId, ZoneIp)
	  VALUES (?, ?, ?);
	`
	_, err := utils.Db.Exec(sql, name, id, ip)
	if err != nil {
		panic(err)
	}
	return err == nil
}
