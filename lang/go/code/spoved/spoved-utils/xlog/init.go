package xlog

func Init() {
	logger := New()
	SetLogger(logger)
}
