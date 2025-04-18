### c项目结构示例

* *结构*
```
c-project-example
|—— bin/
|   |—— app
|
|—— build/
|
|—— include/
|   |—— module.h
|   |—— ...
|
|—— lib/
|
|—— src/
|   |—— main.c
|   |—— module.c
|   |—— ...
|
|—— Makefile
|—— README.md
```

* *使用*
```
  - 构建: make
  - 清理: make clean
```

* *三方库*
```
  - OpenSSL：用于加密和解密数据的开源加密库。
  - SQLite：轻量级的关系型数据库管理系统，可嵌入到应用程序中。
  - libcurl：用于创建和管理HTTP、FTP等协议的客户端的开源库。
  - GTK+：用于构建图形用户界面 (GUI) 的跨平台工具包。
  - zlib：可压缩和解压缩数据的开源库。
  - SDL：简单直接的多媒体库，可用于开发游戏等交互式应用程序。
  - Libuv：用于事件驱动的非阻塞I/O的跨平台库。
  - Libevent：事件通知库，允许高效地处理大量并发网络连接。
  - ncurses：用于创建交互式终端应用程序的库。
  - GMP：用于精确数字计算的数学库。
```
