package codec

import "errors"

var (
    ErrInvalidData       = errors.New("invalid data format")
    ErrInsufficientData  = errors.New("insufficient data to decode")
    ErrEncodingFailed    = errors.New("encoding failed")
    ErrDecodingFailed    = errors.New("decoding failed")
)