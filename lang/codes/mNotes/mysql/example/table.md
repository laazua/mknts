###### table

* *创建表*
```
    CREATE TABLE tb_name
    (
        字段1  数据类型  [列级别约束条件]  [默认值],
        字段2  数据类型  [列级别约束条件]  [默认值],
        ...
        [表级别约束条件]
    );

    -- 例子
    CREATE TABLE student
    (
        id    INT(100),
        name  VARCHAR(64),
        score FLOAT
    );
```

* *单字段主键约束*
```
    CREATE TABLE student
    (
        id    INT(100) PRIMARY KEY,
        name  VARCHAR(64),
        score FLOAT
    );


    CREATE TABLE student
    (
        id    INT(100),
        name  VARCHAR(64),
        score FLOAT,
        PRIMARY KEY(id)
    );
```

* *多字段主键约束*
```
    CREATE TABLE student
    (
        id    INT(100),
        name  VARCHAR(64),
        score FLOAT,
        PRIMARY KEY(id, name)
    );
```

* *使用外键约束*
```
    -- 外键用于在两张表之间建立联系,可以是一列或者多列,一张表可以有多个外键
    -- 外键对应另一张表的主键
    -- 主键所在的表是主表,外键所在的表是从表

    CREATE TABLE teacher
    (
        id     INT(100) PRIMARY KEY,
        name   VARCHAR(64),
        sex    VARCHAR(64)
    );

    CREATE TABLE student 
    (
        id        INT(48),
        name      VARCHAR(64),
        classID   INT(24),
        score FLOAT,
        CONSTRAINT fk_teacher FOREIGN KEY(classID) REFERENCES teacher(id)
    )
    -- 在表student中添加了名为fk_teacher的外键约束,外键名为classID,其依赖于表teacher中的主键id
    -- 关联字段(即主键和外键)的数据类型必须一致
```

* *非空约束*
```
    -- 非空约束是指在向表中添加数据时,如果字段已经约束为非空,但是在添加数据时没有写入数据,则会报错
    -- 字段名  数据类型  NOT NULL
    CREATE TABLE student
    (
        name  VARCHAR(64) NOT NULL
    )
```

* *唯一性约束*
```
    -- 唯一性约束要求该列唯一,允许为空,但是只能出现一个空值.唯一性约束可以确保该列不出现重复值
    -- 字段名  数据类型  UNIQUE
    -- 一张表中可以将多个字段声明为唯一性约束
    CREATE TABLE student
    (
        name  VARCHAR(64) UNIQUE
    )
    或者
    CREATE TABLE student
    (
        name  VARCHAR(64),
        CONSTRAINT STH UNIQUE(name)
    )
```

* *使用默认约束*
```
    -- 指定某列的默认值
    -- 字段名  数据类型  DEFAULT 默认值
    CREATE TABLE student
    (
        name  VARCHAR(64) DEFAULT "test"
    )
```

* *字段自增约束*
```
    -- 字段必须为主键的一部分
    -- 字段名  数据类型  AUTO_INCREMENT
     CREATE TABLE student
    (
        id    INT(4)  AUTO_INCREMENT     # INT(4)中的4表示显示的数字的宽度,与大小无关
        name  VARCHAR(64) UNIQUE
    )    
```

* *查看表结构*
```
    DESC tb_name
    SHOW CREATE TABLE tb_name
```

--------------------------------------------------

* *修改表名*
```
    -- [TO] 表示可以省略
    ALTER TABLE old_tb RENAME [TO] new_tb
```

* *修改字段数据类型*
```
    ALTER TABLE tb_name MODIFY <字段名> <数据类型>
    ALTER TABLE student MODIFY name VARCHAR(128)
```

* *修改字段名*
```
    ALTER TABLE <表名> CHANGE <旧字段名> <新字段名> <数据类型>
```

* *添加字段*
```
    -- FIRST表示在表的第一列添加字段,AFTER 在某个字段后添加字段
    ALTER TABLE <表明> ADD <新字段名> <数据类型> [约束条件] [FIRST|AFTER 已存在字段名]
```

* *删除字段*
```
    ALTER TABLE <表名> DROP <字段名>
```

* *修改表的存储引擎*
```
    ALTER TABLE <表名> DEGINE=<新存储引擎>
```

* *删除表的外键约束*
```
    ALTER TABLE <表名> DROP FOREIGN KEY <外键约束名>
```

* *删除表*
```
    DROP TABLE [IF EXISTS] <表名>
```

* *删除被关联的表*
```
    -- 先解除外键约束
    ALTER TABLE <表名> DROP FOREIGN KEY <外键名>
    -- 删除表
    DROP TABLE <表名>
```
