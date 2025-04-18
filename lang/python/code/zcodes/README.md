### zcodes

- 说明
1. python项目代码组织
2. protocols是接口协议相关代码
3. implements是实现接口协议相关代码
4. services是实现逻辑相关代码
5. implements中的实现依赖于protocols中的协议约定

- 运行
1. python setup.py develop
2. python -m src.zo