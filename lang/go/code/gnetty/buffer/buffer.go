package buffer

import (
    "sync"
)

// ByteBuffer 字节缓冲区
type ByteBuffer struct {
    data  []byte
    read  int
    write int
    mu    sync.RWMutex
}

// NewByteBuffer 创建新的字节缓冲区
func NewByteBuffer(capacity int) *ByteBuffer {
    return &ByteBuffer{
        data:  make([]byte, capacity),
        read:  0,
        write: 0,
    }
}

// Write 写入数据
func (b *ByteBuffer) Write(data []byte) error {
    b.mu.Lock()
    defer b.mu.Unlock()

    // 检查容量
    needed := b.write + len(data)
    if needed > len(b.data) {
        // 扩容
        newCapacity := len(b.data) * 2
        for newCapacity < needed {
            newCapacity *= 2
        }
        newData := make([]byte, newCapacity)
        copy(newData, b.data[:b.write])
        b.data = newData
    }

    copy(b.data[b.write:], data)
    b.write += len(data)
    return nil
}

// Read 读取数据
func (b *ByteBuffer) Read(length int) []byte {
    b.mu.RLock()
    defer b.mu.RUnlock()

    if b.read+length > b.write {
        length = b.write - b.read
    }

    if length <= 0 {
        return nil
    }

    return b.data[b.read : b.read+length]
}

// Peek 查看数据但不移动指针
func (b *ByteBuffer) Peek(length int) []byte {
    b.mu.RLock()
    defer b.mu.RUnlock()

    if b.read+length > b.write {
        length = b.write - b.read
    }

    if length <= 0 {
        return nil
    }

    result := make([]byte, length)
    copy(result, b.data[b.read:b.read+length])
    return result
}

// Skip 跳过指定长度的数据
func (b *ByteBuffer) Skip(length int) {
    b.mu.Lock()
    defer b.mu.Unlock()

    if b.read+length > b.write {
        length = b.write - b.read
    }

    b.read += length

    // 整理缓冲区
    if b.read == b.write {
        b.read = 0
        b.write = 0
    } else if b.read > len(b.data)/2 {
        // 当读指针超过一半时，整理数据
        copy(b.data, b.data[b.read:b.write])
        b.write -= b.read
        b.read = 0
    }
}

// Readable 获取可读字节数
func (b *ByteBuffer) Readable() int {
    b.mu.RLock()
    defer b.mu.RUnlock()
    return b.write - b.read
}

// Clear 清空缓冲区
func (b *ByteBuffer) Clear() {
    b.mu.Lock()
    defer b.mu.Unlock()
    b.read = 0
    b.write = 0
}

// Bytes 获取所有数据
func (b *ByteBuffer) Bytes() []byte {
    b.mu.RLock()
    defer b.mu.RUnlock()

    result := make([]byte, b.write-b.read)
    copy(result, b.data[b.read:b.write])
    return result
}