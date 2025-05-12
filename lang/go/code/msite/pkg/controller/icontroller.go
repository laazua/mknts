package controller

import (
	"msite/pkg/router"
)

type Controller interface {
	Name() string
	InitRoute(*router.Router)
}
