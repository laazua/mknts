package main

// go自带库实现大文件下载服务器
func TestDownLoadBigFileOne(t *Testing.T) {
    // 所下载文件路径
    fp := "/data/files/some_file"
    http.HandleFunc(fp, func(w http.ResponseWriter, r *http.Request) {
      http.ServeFile(w, r, fp)
    })
    err := http.ListenAndServer(":9999", nil)
    assert.NoError(t, err)
}

// gin实现大文件下载服务器
func TestDownLoadBigFileTow(t *Testing.T) {
    fp := "/data/files/some_file"
    g := gin.Default()
    g.GET(fp, func(ctx *gin.Context) {
        http.ServeFile(ctx.Writer, ctx.Request, fp)
    })
    g.Run(":9999")
}

// 单文件数据流方式(推荐)
func TestDownLoadBigFileThree(t *Testing.T) {
    fp := "/data/files/some_file"
    http.HandleFunc(fp, func(w http.ResponseWriter, r *http.Request) {
        // 获取一个文件句柄
      fd, _ := os.Open(fp)
      defer fd.Close()
      
      info, _ := fd.Stat()
      http.ServeContent(w, r, fp, info.ModTime(), fd)
    })
  http.ListenAndServe(":9999", nil)
}
