### sshd + shell
```
  -- 架构:
     运维服+游戏服

  -- 运维服
     目录结构
     /root/yunwei
           ├── client
           │   ├── all_zones.sh
           │   ├── games.sh
           │   ├── init_game_system.sh
           │   ├── iptables.sh
           │   ├── monitor.sh
           │   ├── open_serve.sh
           │   ├── second_crontab.sh
           │   ├── serve_msg.sh
           │   ├── some_zones.sh
           │   ├── svn_client_md5.py
           │   └── svn_game_md5.py
           ├── combine_zone.sh
           ├── combineZone.sh.bak
           ├── README.md
           └── server
                ├── mg.cnf
                └── zones_mg.sh 
  
   -- svn仓库目录结构(client)
     /home/test/
             |- cfiles_md5.txt  
             |- conf/  
             |- config.json  
             |- create_md5.py (svn客户端计算文件md5值)
             |- createMd5.py  
             |- gameser-beta  
             |- games.sh
     

  -- 游戏服
     目录结构
     /data/game/syfdev_syf_1015/
                             |- cfiles_md5.txt  
                             |- conf/  
                             |- config.json  
                             |- createMd5.py  
                             |- gameserv1015  
                             |- games.sh  
                             |- log/  
                             |- tmp/
                             |- vlog/
    /root/scripts/
                |- monitor.sh
                |- secondCrontab.sh
                |- iptables.sh

  --初始化机器步骤
    1. initGameSystem.sh
    2. 运维服ssh配置/root/.ssh/config文件
```
