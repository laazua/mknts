//go 中的继承: 匿名组合
package typeSystem

type Base struct {
	Name  string
}

func (b *Base) Foo() {
	//...
}

func (b *Base) Bar() {
	//...
}

//"继承"Base类
type Foo struct {
	Base
	//...
}

//改写Bar()方法,该方法实现时先调用了基类的Bar()方法
//没有改写Far()方法,则f.Foo()和f.Base.Foo()效果一样
func (f *Foo) Bar() {
	f.Base.Bar()
	//...
}

/*
type Foo struct {
    ...  //其他成员
    Base   //这里定义的Foo与上面的不同之处在于成员属性在内存上的布局不一样
}


以指针的形式"派生",Foo创建实例的时候,需要外部提供一个Base类实例的指针
type Foo struct {
    *Base
    ...
}

匿名字段的成员名字和派生类包含同一个名字时"父类字段名称会被隐藏起来"
type X struct {
    Name  string
}

type Y struct {
    X
    Name string
}
即 X.Name被隐藏

*/