package controller

import (
	"stdhttp/pkg/router"
)

type Controller interface {
	Name() string
	InitRoute(*router.Router)
}
