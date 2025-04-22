class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be less than -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


# 创建一个温度对象
temp = Temperature(25)

# 访问 celsius 属性
print(temp.celsius)  # 输出 25

# 修改 celsius 属性
temp.celsius = 30
print(temp.celsius)  # 输出 30

# 尝试设置不合法的温度
try:
    temp.celsius = -300
except ValueError as e:
    print(e)  # 输出 "Temperature cannot be less than -273.15°C"

# 访问 fahrenheit 属性
print(temp.fahrenheit)  # 输出 86.0

# 修改 fahrenheit 属性
temp.fahrenheit = 95
print(temp.celsius)  # 输出 35
