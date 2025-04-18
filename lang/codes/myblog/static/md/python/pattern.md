## ***常用设计模式***

* *简单工厂模式*
* > 优点：隐藏了对象创建的实现细节，客户端不需要修改代码
* > 缺点：违反了单一职责原则，将创建逻辑都汇集到一个工厂类中，当添加新产品时，需要修改工厂类代码，违反了开闭原则
```
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """接口"""
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    """实现接口"""
    def pay(self, money):
        print("alipay {money}".format(money=money))


class WechatPay(Payment):
    """实现接口"""
    def pay(self, money):
        print("wechatpay {money}".format(money=money))


class PaymentFactory:
    """工厂类生产指定的类"""
    def create_payment(self, method):
        if method == "alipay":
            return AliPay()
        elif method == "wechat":
            return WechatPay()
        else:
            raise TypeError("No such payment named {method}".format(method=method))


if __name__ == '__main__':
    pf = PaymentFactory()
    py = pf.create_payment('alipay')
    py.pay(200)
```

* *工厂方法模式*
* > 有点：每个具体产品都有对应的一个具体工厂类, 不需要修改工厂类代码，隐藏了对象创建的细节
* > 缺点：每增加一个具体类，就必须增加一个相应的具体工厂类
```
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """接口"""
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    """实现接口"""
    def pay(self, money):
        print("alipay {money}".format(money=money))


class WechatPay(Payment):
    """实现接口"""
    def pay(self, money):
        print("wechatpay {money}".format(money=money))


class PaymentFactory(metaclass=ABCMeta):
    """工厂类接口"""
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    """实现工厂类接口"""
    def create_payment(self):
        return AliPay()


class WechatpayFactory(PaymentFactory):
    """实现工厂类接口"""
    def create_payment(self):
        return WechatPay()


if __name__ == '__main__':
    pf = AlipayFactory()
    py = pf.create_payment()
    py.pay(300)

```

* *抽象工厂模式*
* > 定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
* > 与工厂方法模式相比，抽象工厂模式中的每个具体产品都生产一套产品。
* > 有点：将客户端与类的具体实现分离，每个工厂创建了一个完整的产品系列，有利于产品的一致性。
* > 缺点：难以支持新种类的(抽象)产品。
```
from abc import ABCMeta, abstractmethod


# ----------抽象产品----------
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class Cpu(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class Os(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ----------抽象工厂-----------
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ----------具体产品-------------
class XiaomiShell(PhoneShell):
    def show_shell(self):
        print("小米手机壳")


class HuaweiShell(PhoneShell):
    def show_shell(self):
        print("华为手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCpu(Cpu):
    def show_cpu(self):
        print("骁龙cpu")


class MediaTekCpu(Cpu):
    def show_cpu(self):
        print("联发科cpu")


class AppleCpu(Cpu):
    def show_cpu(self):
        print("苹果cpu")


class AndroidOs(Os):
    def show_os(self):
        print("安卓系统")


class IOs(Os):
    def show_os(self):
        print("IOS系统")


# -------------具体工厂------------
class XiaomiFactory(PhoneFactory):
    def make_shell(self):
        return XiaomiShell()

    def make_cpu(self):
        return SnapDragonCpu()

    def make_os(self):
        return AndroidOs()


class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return HuaweiShell()

    def make_cpu(self):
        return MediaTekCpu()

    def make_os(self):
        return AndroidOs()


# ----------客户端-----------------
class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(shell, cpu, os)


if __name__ == "__main__":
    xiaomi = make_phone(XiaomiFactory())
    xiaomi.show_info()
```

* *建造者模式*
* > 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
* > 优点：隐藏了一个产品的内部结构和装配过程，将构造代码与表示代码分开，可以对构造过程进行更精细的控制。

```
from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self):
        self._arm = None
        self._body = None
        self._foot = None

    @property
    def arm(self):
        return self._arm

    @arm.setter
    def arm(self, value):
        self._arm = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    @property
    def foot(self):
        return self._foot

    @foot.setter
    def foot(self, value):
        self._foot = value

    def __str__(self):
        return "%s %s %s" % (self.arm, self.body, self.foot)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_foot(self):
        pass


class ZhangsanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_arm(self):
        self.player.arm = "花手臂"

    def build_body(self):
        self.player.body = "强壮身体"

    def build_foot(self):
        self.player.foot = "大长腿"


class PlayerDirector:
    """控制组装顺序"""
    def build_player(self, builder):
        builder.build_arm()
        builder.build_body()
        builder.build_foot()
        return builder.player


if __name__ == "__main__":
    # 客户端
    builder = ZhangsanBuilder()
    diretor = PlayerDirector()
    player = diretor.build_player(builder)
    print(player)
```

* *单例模式*
* > 优点：对唯一实例的受控访问，保证一个类只有一个实例，并提供一个访问它的全局访问点。
```
class Singleton:
    def __new__(cls, *arg, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Person(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    p1 = Person('张三')
    p2 = Person('李四')

    print(p1.name)
    print(p2.name)

    print(id(p1))
    print(id(p2))
```

* *适配器模式*
```
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付{money}".format(money=money))


class Wechatpay(Payment):
    def pay(self, money):
        print("微信支付{monye}".format(money=money))


class Bankpay:
    def cost(self, money):
        print("银联支付{money}".format(money=money))


class PayMentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)



if __name__ == "__main__":
    p = PayMentAdapter(Bankpay())
    p.pay(300)
```

* *桥模式*
* > 优点：抽象和实现分离，优秀的扩展能力
```
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        # rectangle逻辑
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"
    def draw(self):
        # circle逻辑
        self.color.paint(self)


class Line(Shape):
    name = "直线"
    def draw(self):
        # line逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色 %s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色 %s" % shape.name)


class Blue(Color):
    def paint(self, shape):
        print("蓝色 %s" % shape.name)


if __name__ == "__main__":
    shape = Rectangle(Red())
    shape.draw()
```

* *组合模式*
```
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点 (%s, %s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线 [%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add (self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("-----复合图形------")
        for g in self.children:
            g.draw()
        print("-----复合图形------")


if __name__ == "__main__":
    p1 = Point(1, 2)
    l1 = Line(Point(3, 4), Point(5, 6))
    l2 = Line(Point(7, 8), Point(6, 6))
    pic = Picture([p1, l1, l2])
    pic.draw()
```

* *外观模式*
```
class CPU:
    def run(self):
        print("cpu run...")

    def stop(self):
        print("cpu stop...")


class Disk:
    def run(self):
        print("disk run...")

    def stop(self):
        print("disk stop...")


class Memory:
    def run(self):
        print("memory run..")


    def stop(self):
        print("memory stop...")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

if __name__ == "__main__":
    c = Computer()
    c.run()
    c.stop()
```

* *观察者模式(发布订阅模式)*
* > 对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都得到通知并被自动更新。
* > 角色：
* >> 抽象主题
* >> 具体主题(发布者)
* >> 抽象观察者
* >> 具体观察者(订阅者)
```
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者(订阅者)接口"""
    @abstractmethod
    def update(self, notice):
        """
        notice是一个Notice类的对象
        """
        pass


class Notice:
    """抽象发布者"""
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        """推送功能"""
        for observer in self.observers:
            observer.update(self)


class StaffNotice(Notice):
    """具体发布者"""
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == "__main__":
    notice = StaffNotice("初始公司信息")
    s1 = Staff()
    s2 = Staff()
    notice.attach(s1)
    notice.attach(s2)
    notice.company_info = "公司业绩下滑，掺不忍睹"
    print(s1.company_info)
    print(s2.company_info)
    notice.detach(s1)
    notice.company_info = "明天加班"
    print("----------------------")
    print(s1.company_info)
    print(s2.company_info)
```