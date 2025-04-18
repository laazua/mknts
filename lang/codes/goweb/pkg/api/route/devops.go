package route

import (
	"gweb/pkg/dto"
	"gweb/pkg/utils"
	"log"
	"net/http"
	"sync"
)

var wg sync.WaitGroup

func ManZone(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		return
	}
	log.Println("Path: /ops/add Method: POST")
	data, err := utils.ParseZoneBodyData(r)
	if err != nil {
		log.Println(err)
		return
	}

	mch := make(chan interface{}, len(data["zonelist"]))
	wg.Add(len(data["zonelist"]))
	for _, z := range data["zonelist"] {
		if !dto.AddZoneToDb(z.ZoneName, z.ZoneIp, z.ZoneId) {
			return
		}
		callMonion := utils.NewClient(z)
		go callMonion.StartClient(mch)

	}
	chdata := make([]interface{}, 0)
	go func(ch chan interface{}) {
		for {
			select {
			case a := <-ch:
				chdata = append(chdata, a)
			}
			wg.Done()
		}
	}(mch)
	wg.Wait()
	utils.HttpRespse(w, chdata)
}
