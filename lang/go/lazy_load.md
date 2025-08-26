### 懒加载

- **sync.Once**
1. 推荐使用 sync.Once - 简单、线程安全、性能好
```golang
package main

import (
	"fmt"
	"sync"
)

type ExpensiveObject struct {
	Name string
	// 其他昂贵资源
}

type LazyObject struct {
	once   sync.Once
	object *ExpensiveObject
}

func (l *LazyObject) Get() *ExpensiveObject {
	l.once.Do(func() {
		l.object = &ExpensiveObject{Name: "Lazy Instance"}
		// 这里可以执行昂贵的初始化操作
	})
	return l.object
}

func main() {
	lazy := &LazyObject{}

	// 第一次调用会创建对象
	obj1 := lazy.Get()
	// fmt.Println("Object name:", obj1.Name)
	fmt.Printf("%p\n", obj1)

	// 后续调用返回已创建的对象
	obj2 := lazy.Get()
	// fmt.Println("Same object?", obj1 == obj2) // true
	fmt.Printf("%p\n", obj2)
}
```

- **sync.Mutex**
1. 需要复杂的初始化逻辑，使用 互斥锁方案
```golang
package main

import (
	"fmt"
	"sync"
)

type ExpensiveObject struct {
	Name string
	// 其他昂贵资源
}

type LazyObjectMutex struct {
	mu     sync.Mutex
	object *ExpensiveObject
}

func (l *LazyObjectMutex) Get() *ExpensiveObject {
	l.mu.Lock()
	defer l.mu.Unlock()

	if l.object == nil {
		l.object = &ExpensiveObject{Name: "Lazy Instance"}
		// 昂贵的初始化操作
	}
	return l.object
}

func main() {
	lazyObjMux := &LazyObjectMutex{}

	obj1 := lazyObjMux.Get()
	fmt.Printf("%p\n", obj1)

	obj2 := lazyObjMux.Get()
	fmt.Printf("%p\n", obj2)
}
```

- **atomic.Value**
1. 高性能场景，可以考虑 原子操作方案

```golang
package main

import (
	"fmt"
	"sync/atomic"
)

type ExpensiveObject struct {
	Name string
	// 其他昂贵资源
}

type LazyObjectAtomic struct {
	object atomic.Value
}

func (l *LazyObjectAtomic) Get() *ExpensiveObject {
	if obj := l.object.Load(); obj != nil {
		return obj.(*ExpensiveObject)
	}

	// 创建新对象
	newObj := &ExpensiveObject{Name: "Lazy Instance"}

	// 使用 CompareAndSwap 确保线程安全
	if l.object.CompareAndSwap(nil, newObj) {
		return newObj
	}

	// 如果其他线程已经设置了值，返回已存在的对象
	return l.object.Load().(*ExpensiveObject)
}

func main() {
	lazyObj := &LazyObjectAtomic{}

	obj1 := lazyObj.Get()
	fmt.Printf("%p\n", obj1)
	obj2 := lazyObj.Get()
	fmt.Printf("%p\n", obj2)
}
```