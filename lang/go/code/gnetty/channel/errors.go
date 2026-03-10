package channel

import "errors"

var (
    ErrChannelClosed = errors.New("channel is closed")
    ErrHandlerExists = errors.New("handler already exists")
)