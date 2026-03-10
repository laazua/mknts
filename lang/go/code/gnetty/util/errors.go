package util

import "errors"

var (
    ErrPoolClosed = errors.New("pool is closed")
)