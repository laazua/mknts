package prometheus_doc

/*
  -- https://github.com/prometheus/prometheus
	1. prometheus是一个用于监控系统和一些服务的监控系统.它在指定的时间间隔里从配置文件中包含的主机或服务上拉取数据.当一些数据
	   指标达到指定的阈值是就可以触发报警.
	2. prometheus与其他一些监控系统的区别特征是:
	   1) 多维数据模型(由度量标准名称和键/值集定义时间序列)
	   2) 可以利用PromQL这个强大的查询语言进行维度查询
	   3) 单个服务节点独立,不依赖任何分布式存储
	   4) 是一个时间序列收集的HTTP拉取模型
	   5) 可以通过中间网关(gateway)进行批处理来推送时间序列值
	   6) 通过服务发现或静态配置发现目标
	   7) 多种模式的图形和仪表盘支持
	   8) 支持分层和水平联合
	3. 该项目下包含的目录，如下:
	   1) cmd目录, 程序的入口和promtool规则校验工具的源码
	   2) discovery目录, 服务发现模块的逻辑源码
	   3) config目录, 来解析yaml配置文件，其下的testdata目录中有非常丰富的各个配置项的用法和测试
	   4) notifier目录，负责通知管理，规则触发告警后，由这里通知服务发现的告警服务
	   5) pkg目录, 是内部的一些依赖
	   6) prompb目录, 定义了三种协议，用来处理远程读写的远程存储协议，处理tsdb数据的rpc通信协议，被前两种协议使用的types协议，例如使用es做远程读写，需要远程端实现远程存储协议(grpc)，远程端获取到的数据格式来自于types中，就是这么个关系
	   7) promql目录, 处理查询用的promql语句的解析
	   8) rules目录, 负责告警规则的加载、计算和告警信息通知
	   9) scrape目录, 是核心的根据服务发现的targets获取指标存储的模块
	   10) storge目录，处理存储，其中fanout是存储的门面，remote是远程存储，本地存储用的下面一个文件夹
       11) tsdb时序数据库，用作本地存储
	4. 更多详细信息参考: prometheus.io

  -- https://github.com/prometheus/client_golang
	1. 这是prometheus的go客户端库代码包.它包含两部分,一部分是用于检测应用程序的代码,一部分是用于创建于Prometheus HTTP API
	   通信的客户机
	2. 该库代码包下面包含三个目录api, examples, promethues
	   1) api目录，包含了给客户端调用的Prometheus HTTP API，它允许你用go代码从Prometheus的服务端查询时序数据
	   2) examples目录, 包含了一些简单的api调用示例代码
	   3) prometheus目录, 包含了一些工具集代码库,更多详细信息参考官网
*/
