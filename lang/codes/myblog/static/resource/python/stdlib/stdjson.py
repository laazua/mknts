import json


# python对象格式化成一个json字符串
person = {"name": "zhangsan", "age": 18, "tel": ["13478735209", "15287364995"], "isonly": True}

jsonStr = json.dumps(person)
print(jsonStr)


# python对象写入文件
with open("person.json", "w") as fd:
    json.dump(person, fd, indent=4, sort_keys=True)


# json字符串转化成python对象
js = '{"name": "zhangsan", "age": 18, "tel": ["13478735209", "15287364995"], "isonly": true}'
print(json.loads(js))

# 将json文件转化成python对象
with open('person.json', 'r') as fd:
    print(json.load(fd))
