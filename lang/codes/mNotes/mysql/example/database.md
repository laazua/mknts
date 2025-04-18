###### database

* **查看数据库**
```
    mysql> SHOW DATABASES;
```
* **创建数据库**
```
    mysql> CREATE DATABASE db_name;
```

* **查看数据库定义**
```
    mysql> SHOW CREATE DATABASE db_name;
```

* **查看数据库中的表**
```
    mysql> SHOW DATABASES;
```

* **删除数据库**
```
    DROP DATABASE db_name;
```

* **查看系统表类型**
```
    SELECT DISTINCT(ENGINE) FROM information_schema.tables;
```

* **查看数据库默认编码**
```
    SHOW VARIABLES LIKE 'character_set_database'
```