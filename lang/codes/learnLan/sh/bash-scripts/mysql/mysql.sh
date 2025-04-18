#!/bin/bash

# 参考: https://www.mysqlzh.com/

echo "
    # 多表查询, 结果table1 * table2
    SELECT table1.name, table1.sex, table1.age, table2.name, table2.role FROM table1, table2;
    SELECT t1.name, t1.sex, t1.age, t2.name, t2.role FROM table1 t1, table2 t2; 
    SELECT table1.name, table2.name, table3.name FROM table1, table2, table3 WHERE table1.id=table2.id AND table2.id=table3.id;

    # inner join: 取两张表中存在连接匹配关系的记录
    SELECT * FROM table1 inner join table2 on condition;
    # left join: 条件成立,则把所有的数据查询出来, 否则,table1中的数据全部查询出来,table2中的字段没有数据就为null
    SELECT * FROM table1 left join table2 on condition;
    # right join: 与left join相反
    SELECT * FROM table1 right join table2 on condtion;
    # 交叉连接:
    SELECT * FROM table1 cross join table2 on condition;
"