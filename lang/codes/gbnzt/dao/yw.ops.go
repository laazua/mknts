package dao

import "bnzt/models"

type DbZone interface {
	ZoneList() []models.Zone
	AddZone(sz models.Ozs) bool
}

func NewDbZone() DbZone {
	return &dbZone{}
}

type dbZone struct {
	DZone models.Zone
}

// 区服列表
func (d *dbZone) ZoneList() []models.Zone {
	var zone []models.Zone
	if DB.Debug().
		Select("zone", "channame", "ip").
		Find(&zone).Error != nil {
		return nil
	}
	return zone
}

// 添加区服
func (d *dbZone) AddZone(sz models.Ozs) bool {
	return DB.Create(models.Zone{
		Ip:       sz.Ip,
		ChanName: sz.ChanName,
		Zone:     sz.Zone,
	}).Error == nil
}
