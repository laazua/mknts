package utils

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

type LoginParam struct {
	Username string
	Password string
}

type ZoneParam struct {
	ZoneIp   string `json:"ZoneIp"`
	ZoneId   int    `json:"ZoneId"`
	ZoneName string `json:"ZoneName"`
	Target   string `json:"Target"`
}

type ManZoneParam struct {
	ZoneList []ZoneParam `json:"ZoneList"`
}

func ParseZoneBodyData(r *http.Request) (map[string][]ZoneParam, error) {
	data, err := ioutil.ReadAll(r.Body)
	p := make(map[string][]ZoneParam)
	if err != nil {
		return nil, err
	}
	if err := json.Unmarshal([]byte(data), &p); err != nil {
		return nil, err
	} else {
		return p, nil
	}
}

func ParseLoginBodyData(r *http.Request) (*LoginParam, error) {
	data, err := ioutil.ReadAll(r.Body)
	var p *LoginParam
	if err != nil {
		return nil, err
	}
	if err := json.Unmarshal([]byte(data), &p); err != nil {
		return nil, err
	}
	return p, nil
}
