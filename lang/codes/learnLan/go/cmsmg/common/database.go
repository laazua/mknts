package common

import (
    "fmt"
    "github.com/jinzhu/gorm"
    "cmsmanager/model"
    "github.com/spf13/viper"
)

func GetDB() *gorm.DB {
    DB := initDB()
    return DB
}

func initDB() *gorm.DB{
    driverName := viper.GetString("database.driverName")
    host := viper.GetString("database.host")
    port := viper.GetString("database.port")
    database := viper.GetString("database.dbname")
    username := viper.GetString("database.username")
    password := viper.GetString("database.password")
    charset := viper.GetString("database.charset")
    args := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=%s&parseTime=true",
        username,
        password,
        host,
        port,
        database,
        charset)
    db, err := gorm.Open(driverName, args)
    if err != nil {
        panic("failed to  connect to database" + err.Error())
    }
    db.AutoMigrate(&model.User{})
    return db
}
