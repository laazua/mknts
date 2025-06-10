### dpsup


- 说明
1. supervisord 创建守护进程的接口
2. 支持新增和删除:  
   POST /api/create  
   json参数: {name: "进程配置文件名称", command: "守护进程执行的启动命令", number: "启动的进程数量"}
   DELETE /api/delte  
   json参数: {name: "进程配置文件名称"}
3. 此接口未作安全认证只能启动在本地回环地址上,供本机调用
4. 启动服务前按照.env.example示例配置在执行启动路径下配置.env文件


- 部署
1. mkdir /etc/dpsup
2. cp .env.example /etc/dpsup/dpsup.conf
3. cp systemd/dpsup.service /usr/lib/systemd/system/dpsup.service
4. systemctl daemon-reload && systemctl start dpsup.service