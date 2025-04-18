//一个类实现了一个接口中的所有方法,则该类就实现了这个接口
package typeSystem

//定义一个File类型,并实现一下方法
type File struct {
	//...
}

func (f *File) Read(buf []byte) (n int, err error) {
	//..
}

func (f *File) Write(buf []byte) (n int, err error) {
	//..
}

func (f *File) Seek(off int64, whence int) (pos int64, err error) {
	//..
}

func (f *File) Close() error {
	//..
}


//如果有以下接口
type IFile interface {
	Read(buf []byte) (n int, err error)
	Write(buf []byte) (n int, err error)
	Seek(off int64, whence int) (pos int64, err error)
	Close() error
}

type IReader interface {
	Read(buf []byte) (n int, err error)
}

type IWriter interface {
	Write(buf []byte) (n int, err error)
}

type ICloser interface {
	Close() error
}

//则可以用IFile类型进行一下操作
var (
	file1 IFile = new(File)
	file2 IReader = new(File)
	file3 IWriter = new(File)
	file4 ICloser = new(File)
)

//类的实现只关心要提供哪些方法,不需要纠结接口的拆分;接口由使用方按需定义,不用事前规划

//接口赋值
//将对象实例赋值给接口(要求该对象实例实现了接口要求的所有方法)
type Integer int

func (a Integer) Less(b Integer) bool {
	return a < b
}

func (a *Integer) Add(b Integer) {
	*a += b
}

type LessAdder interface {
	Less(b Integer) bool
	Add(b Integer)
}

var(
	a Integer = 100
	b LessAdder = &a
	//go会根据函数 func(a Integer) Less(b Integer) bool 自动生成一个新的Less()方法:
	//            func(a *Integer) Less(b Integer) bool {
	//                return (*a).Less(b)
	//            }
)

//将接口赋值给接口(要求两个接口的方法签名一样,次序不一定要一样)
/*
////
package one

type ReadWriter interface {
    Read(buf []type) (n int, err error)
    Write(buf []type) (n int, err error)
}

////
package two

type IStream interface {
    Write(buf []type) (n int, err error)
    Read(buf []type) (n int, err error)
}

one.ReadWriter 和 two.IStream 都定义了Read() 和 Write()方法,则这两个接口本质一样,任何实现了one.ReadWriter接口的类都实现了two.IStream接口
可以进行如下操作
var (
    f1 two.IStream = new(File)
    f2 one.ReadWriter = f1
    f3 two.IStream = f2
)

接口赋值不要求两个接口必须等价,如果接口A的方法列表是接口B的方法列表的子集,那么接口B可以赋值给接口A
例如,有如下接口:
type Writer interface {
    Write(buf []type) (n int, err error)
}
则可以将one.ReadWriter 和 two.IStream接口的实例赋值给Writer接口:
var f4 two.IStream = new(File)
var f5 Writer = f4

////
接口查询(如何将上面的Writer接口转换为two.IStream接口?)
var f6 Writer = ...
if f7, ok := f6.(two.IStream); ok {
    ...
}

////
类型查询
var v1 interface{} = ...
switch v := v1.(type) {
    case int:
        ...
    case string:
        ...
}

////
接口组合
type Writer interface {
    ...
}

type Reader interface {
    ...
}

type ReadWriter interface {
    //ReadWriter接口组合了Writer和Reader的方法
    Writer
    Reader
}
*/
