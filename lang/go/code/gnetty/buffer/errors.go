package buffer

import "errors"

var (
    ErrInsufficientData = errors.New("insufficient data in buffer")
)