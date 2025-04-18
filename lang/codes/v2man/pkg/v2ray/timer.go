package v2ray

import (
	"sync"
	"time"
)

type Timer struct {
	ticker *time.Ticker
	quit   chan struct{}
	wg     sync.WaitGroup
	job    func()
}

func NewTimer(interval time.Duration, job func()) *Timer {
	return &Timer{
		ticker: time.NewTicker(interval),
		quit:   make(chan struct{}),
		job:    job,
	}
}

func (t *Timer) Start() {
	t.wg.Add(1)
	go func() {
		defer t.wg.Done()
		for {
			select {
			case <-t.ticker.C:
				t.job()
			case <-t.quit:
				t.ticker.Stop()
				return
			}
		}
	}()
}

func (t *Timer) Stop() {
	close(t.quit)
	t.wg.Wait()
}
