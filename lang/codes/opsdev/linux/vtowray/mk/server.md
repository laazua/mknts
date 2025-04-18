### v2配置

- 描述
1. 版本: V2 5.20.0

- 服务端配置
```json
{
  "log": {
    "loglevel": "info"
 //   "access": "/var/log/v2/access.log",
 //   "error": "/var/log/v2/error.log"
  },
  "api": {
    "tag": "api",
    "services": [
      "StatsService"
    ]
  },
  "dns": {},
  "stats": {},
  "routing": {},
  "policy": {
    "levels": {
      "0": {
        "statsUserUplink": true,
        "statsUserDownlink": true
      }
    },
    "system": {
      "statsInboundUplink": true,
      "statsInboundDownlink": true
    }
  },
  "reverse": {},
  "inbounds": [
    {
      "protocol": "vmess",
      "port": 8888,
      "settings": {
        "clients": [
          {
            "id": "cc8b8eb8-0849-420a-8c66-4d84f937cb28",
            "alterId": 0
          },
          {
            "id": "cd7b8eb8-0849-420a-8c66-4d84f939cb29",
            "alterId": 0
          }
        ]
      },
      "sniffing": {
        "enabled": true,
        "destOverride": [
            "http",
            "tls"
        ],
        "metadataOnly": false
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {}
    }
  ],
  "transport": {}
}
```

- 客户端配置
```json
{
    "inbounds": [
	{
            "port": 8080,  // HTTP 代理端口
            "protocol": "http",  // HTTP 协议
            "settings": {},
            "sniffing": {
            "enabled": true,
                "destOverride": ["http", "tls"]
            }
        },
	{
	    "port": 8082,
	    "protocol": "socks",
	    "settings": {}
	}
    ],
    "outbounds": [
        {
            "protocol": "vmess",
            "settings": {
                "vnext": [
                    {
                        "address": "xxx.xxx.xxx.xxx", // 服务器地址，请修改为你自己的服务器 ip 或域名
                        "port": 8888, // 服务器端口
                        "users": [
                            {
                                "id": "cd7b8eb8-0849-420a-8c66-4d84f939cb29"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "protocol": "freedom",
            "tag": "direct"
        }
    ],
    "routing": {
        "domainStrategy": "IPOnDemand",
        "rules": [
            {
                "type": "field",
                "ip": [
                    "geoip:private"
                ],
                "outboundTag": "direct"
            }
        ]
    }
}
```

- windows客户端
1. https://github.com/2dust/v2xxxx