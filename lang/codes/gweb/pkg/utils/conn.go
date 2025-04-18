package utils

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"log"
	"net"
)

type DataCryt struct {
	Crypto *Cryto
}

type ZoneParam struct {
	ZoneIp   string `json:"ZoneIp"`
	ZoneId   int    `json:"ZoneId"`
	ZoneName string `json:"ZoneName"`
	Target   string `json:"Target"`
}

type ConnData struct {
	Zone *ZoneParam
	Msg  string
}

func NewDataHandle() DataCryt {
	return DataCryt{
		Crypto: NewCryto(),
	}
}

func (c DataCryt) PacketData(data []byte) []byte {
	enData, err := c.Crypto.EnData(data)
	if err != nil {
		panic(err)
	}
	length := int32(len(enData))
	buffer := bytes.NewBuffer([]byte{})
	binary.Write(buffer, binary.LittleEndian, length)
	binary.Write(buffer, binary.LittleEndian, []byte(enData))
	return buffer.Bytes()
}

func (c DataCryt) UnpacketData(reader *bufio.Reader) string {
	// 数据流中的前4位是数据长度的值
	lenByte, _ := reader.Peek(4)
	lenBuff := bytes.NewBuffer(lenByte)
	var length int32
	binary.Read(lenBuff, binary.LittleEndian, &length)
	if int32(reader.Buffered()) < length+4 {
		return ""
	}
	packet := make([]byte, int(4+length))
	_, err := reader.Read(packet)
	if err != nil {
		return ""
	}
	deData, err := c.Crypto.DeData(string(packet[4:]))
	if err != nil {
		panic(err)
	}
	return string(deData)
}

func (c DataCryt) ReadConnData(conn net.Conn) string {
	reader := bufio.NewReader(conn)
	data := c.UnpacketData(reader)
	if data == "" {
		return ""
	}
	return data
}

func (c DataCryt) WriteConnData(conn net.Conn, data []byte) {
	n, err := conn.Write(c.PacketData(data))
	if err != nil {
		log.Println("write conn data err: ", err)
		return
	}
	log.Printf("Send: %d byte message", n)
}
