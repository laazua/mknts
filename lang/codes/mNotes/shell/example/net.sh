#!/bin/bash

echo "
### 三次握手
# client发送一个SYN标志的TCP报文给server请求连接
# server响应client发送一个SYN+ACK标志的报文给client
# client回应server一个ACK报文

### 四次挥手
# TCP连接是双全工的,因此每个方向都必须单独进行关闭.
# 原则上是当一方完成数据发送任务时就发送一个FIN来终止这个方向的连接.
# 收到一个FIN只意味着这一方向上没有数据流动了,一个TCP连接在收到一个FIN后任能发送数据.
# 主动关闭的一方将执行主动关闭,而另一方将执行被动关闭.
# 过程如下:
# TCP客户端发送一个FIN,用来关闭客户端到服务器的数据传送.
# 服务端收到这个FIN,回一个ACK，确认序号为收到的序号加1.
# 服务端关闭客户端的连接,发送一个FIN给客户端.
# 客户端发回一个ACK报文确认,并将确认序号设置为收到的序号加1.

### 以上两个过程TCP的状态如下:
# CLOSED: 表示初始状态
# LISTEN: 表示服务端处于监听状态
# SYN_RCVD: 表示接收到了一个SYN报文,这个状态是三次握手的一个中间状态,很短暂.
# SYN_SENT: 与SYN_RCVD状态相呼应,当客户端执行CONNECT连接时,会发送SYN报文,随即进入SYN_SENT状态.
# ESTABLISHED: 表示已经建立连接了.
# FIN_WAIT_1: 表示正在等待对方的FIN报文,他时当socket在ESTABLISHED状态时,它想主动关闭连接,于是向对方
#             发送了FIN报文,随机进入了FIN_WAIT_1状态.
# FIN_WAIT_2: 表示在回应了FIN报文后进入的状态(此状态为半连接状态)
# TIME_WAIT: 表示收到对方的FIN报文,并发出了ACK报文,等2MSL后回到CLOSED可用状态
# CLOSSING: 正常情况下,当发送FIN报文后,应该先收到对方的ACK报文,在收到对方的FIN报文,但CLOSING表示发送
#           FIN后直接收到对方的FIN报文.
# CLOSE_WAIT: 表示正在等待关闭,当对方发送一个FIN报文给自己时,会回一个ACK报文,随即进入CLOSE_WAIT状态
# LAST_ACK: 被动关闭的一方在发送FIN报文后，最后等待对方的ACK报文.
"  
