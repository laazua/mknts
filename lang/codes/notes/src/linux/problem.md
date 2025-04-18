# 常见问题

---

- journalctl -u redis  
  redis.service: main process exited, code=killed, status=9/KILL  
  出现以上描述,是因为系统资源使用过高,导致系统杀死了 redis.service 服务

- 日志统计
  awk '{print $N}' logfile.txt | sort | uniq -c | sort -nr
