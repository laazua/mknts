# count.es

* **描述**
  - 统计ES集群中站点访问情况,并生成对应的xlsx文件报表.

* **部分示例结果**
  ![图例一](images/screenshot-20240320-090103.png)
  ![图例二](images/screenshot-20240320-090314.png)

* *单元测试*
```
pdm run python -m unittest discover -s tests
```  

* *运行项目*
```
pdm run python -m src.count_es
```