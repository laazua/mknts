### argparse模块

- **简单示例**
1. 代码
```python
import argparse


# 创建 ArgumentParser 对象, 开启帮助选项(默认开启)
parser = argparse.ArgumentParser(description="命令行参数示例", add_help=True)

# 添加位置参数：直接在命令行中给出参数值
parser.add_argument("name", type=str, help="your name")
# 添加可选参数：通常以 -- 开头，后面跟随值，可以在命令行中选择性地提供
parser.add_argument("--age", type=int, default=18, help="your age")

# 解析命令行参数
args = parser.parse_args()

print(f"name: {args.name}, age:{args.age}")
```
2. 使用
```bash
#!/usr/bin/bash

python demo.py -h|--help
python demo.py zhangsan --age 20
```

- **参数分组**
1. 代码
```python
import argparse


# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="命令参数分组示例")

# 分组一
group1 = parser.add_argument_group(title="分组一", description="分组一相关参数")
group1.add_argument("name", type=str, help="你的名字")
group1.add_argument("--age", type=int, default=18, help="你的年龄")

# 分组二
group2 = parser.add_argument_group(title="分组二", description="分组二相关参数")
group2.add_argument("score", type=int, help="你的分数")
group2.add_argument("--grade", type=int, default=1, help="你的班级")

# 创建一组互斥参数组: --verbose 和 --quiet 是互斥的，用户只能选择其中一个参数，不能同时提供两个
group3 = parser.add_mutually_exclusive_group()
group3.add_argument("--verbose", action="store_true", help="输出详细信息")
group3.add_argument("--quit", action="store_true", help="不输出任何信息")

# 解析命令行参数
args = parser.parse_args()

if args.quit:
    print(args.name, args.age, args.score, args.grade)

if args.verbose:
    print(f"name: {args.name}, age: {args.age}, score: {args.score}, grade: {args.grade}")

# 命令行帮助信息会按分组显示，使得命令行界面更加清晰
```
2. 使用
```bash
python demo.py -h|--help
python demo.py zhangsan 20
python demo.py zhangsan --age 20 98 --grade 5
python demo.py zhangsan 20 --age 20
python demo.py zhangsan 20 --age 20 --grade 8
```

- **子命令示例**
1. 代码
```python
import argparse

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="子命令示例")

# 创建子命令解释器: subparser
subparser = parser.add_subparsers(description="子命令解析", dest="cmd")

# 创建add子命令
add_parser = subparser.add_parser("add", help="执行add操作")
add_parser.add_argument("--aa", action="store", type=int, default=0, help="被操作数aa")
add_parser.add_argument("--bb", action="store", type=int, default=0, help="被操作数bb")

# 创建sub子命令
sub_parser = subparser.add_parser("sub", help="执行sub操作")
sub_parser.add_argument("--aa", action="store", type=int, default=0, help="被操作数aa")
sub_parser.add_argument("--bb", action="store", type=int, default=0, help="被操作数bb")

# 解析命令行参数
args = parser.parse_args()

if args.cmd == 'add':
    print(f"add option: aa + bb = {args.aa + args.bb}")
    parser.exit(0, "执行 add option\n")
if args.cmd == 'sub':
    print(f"sub option: aa - bb = {args.aa - args.bb}")
    parser.exit(0, "执行 sub option\n")
# parser.print_usage()
parser.print_help()

# action参数说明: 
# action='store' : 默认行为，存储用户输入的值
# action='store_true' : 布尔类型，若命令行中出现该参数，则为 True，否则为 False
# action='store_false' : 与 store_true 相反，若命令行中出现该参数，则为 False，否则为 True
# action='store_const' : 将常量值存储到参数中
# action='append' : 每次出现该参数时将值追加到列表
# action='append_const' : 将常量值追加到列表
# action='count' : 每次出现该参数时计数加一
# action='version' : 显示版本信息并退出
```
2. 使用
```base
python demo.py -h|--help
python demo.py add -h|--help
python demo.py sub -h|--help
python demo.py add --aa 10 --bb 20
python demo.py sub --aa 66 --bb 35
```