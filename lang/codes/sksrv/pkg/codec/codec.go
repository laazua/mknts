package codec

import (
	"encoding/json"
	"sksrv/pkg/comm"
)

type Codec interface {
	Encode(msg *comm.Message) ([]byte, error)
	Decode(data []byte) (*comm.Message, error)
}

type JsonCodec struct{}

func (c *JsonCodec) Encode(msg *comm.Message) ([]byte, error) {
	return json.Marshal(msg)
}

func (c *JsonCodec) Decode(data []byte) (*comm.Message, error) {
	var msg comm.Message
	err := json.Unmarshal(data, &msg)
	return &msg, err
}
