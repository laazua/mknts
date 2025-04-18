package utils

import (
	"context"

	"github.com/spf13/viper"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var Client *mongo.Client

func InitConfig(name string) {
	if name == "caller" {
		viper.SetConfigName("caller")
	} else {
		viper.SetConfigName("slaver")
	}
	viper.AddConfigPath("./config")
	viper.SetConfigType("yaml")
	if err := viper.ReadInConfig(); err != nil {
		panic(err)
	}
}

func InitMongodb() {
	Client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(viper.GetString("db_url")))
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := Client.Disconnect(context.TODO()); err != nil {
			panic(err)
		}
	}()
}
