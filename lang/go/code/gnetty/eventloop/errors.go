package eventloop

import "errors"

var (
    ErrEventLoopClosed = errors.New("event loop is closed")
)