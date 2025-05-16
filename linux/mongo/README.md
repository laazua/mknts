### mongo

- 创建用户
```
db.createUser(
  {
    user: "zhangsan",
    pwd: "dandf12nkN872n",
    roles: [ 
      { 
        role: "readWrite", 
        db: "dbName" 
      },
      { 
        role: "dbAdmin", 
        db: "dbName"
      }
    ]
  }
)
```
