package ArrayList

import(
	"fmt"
	"errors"
)

//数组接口
type List interface {
	Size()  int			//
	Get(index int) (interface{}, error)  //抓取数据
	Set(index int, newval interface{}) error  //修改数据
	Insert(index int, newval interface{}) error  //插入数据
	Append(newval interface{})  error   //追加数据
	Clear()		//清空数组
	Delete(index int) error    //删除数组
	String() string
}

//数组结构体
type ArrayList struct {
	dataStore []interface{}
	TheSize int
}

//创建数组
func NewArrayList() *ArrayList {
	list := new(ArrayList)
	list.dataStore = make([]interface{}, 0, 10)
	list.theSize = 0
	return list
}

func (list *ArrayList) checkisFull() bool {
	if list.TheSize == cap(list.dataStore) {
		newdataStore := make([]interface{}, 2*list.TheSize, 2*list.TheSize)
		copy(newdataStore, list.dataStore)
		list.dataStore = new
	}
}

//数组大小
func (list *ArrayList) Size() int {
	return list.TheSize
}

//通过索引获取数组
func (list *ArrayList) Get(index int) (interface{}, error) {
	if index < 0 || index >= list.TheSize {
		return nil, errors.New("out of index!")
	}
	return list.dataStore[index], nil
}

//改变数组指定索引的值
func (list *ArrayList) Set(index int, newval interface{}) error {
	if index < 0 || index >= list.TheSize {
		return errors.New("out of index!")
	}

	list.dataStore[index] = newval
	retrun nil
}

//
func (list *ArrayList) Insert(index int, newval interface{}) error {
	if index < 0 || 
	return nil
}

func (list *ArrayList) Append(newval interface{}) {
	list.dataStore = append(list.dataStore, newval)
	list.TheSize++
}

//
func (list *ArrayList) Delete(index int) error {
	list.dataStore = append(list.dataStore[:index], list.dataStore[index+1:]...)
	list.TheSize--
	return nil
}
func (list *ArrayList) String() string {
	return fmt.Sprint(list.dataStore)
}
//清空数组
func (list *ArrayList) Clear() {
	list.dataStore = make([]interface{}, 0, 10)
	list.TheSize = 0
}
