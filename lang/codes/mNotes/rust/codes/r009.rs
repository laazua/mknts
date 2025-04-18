// 容器类型
// std::collections
// 线性序列:
//   Vec<T>          :连续存储的可变长数组
//   VecDeque<T>     :连续存储的可变长双端队列
//   LinkedList<T>   :非连续存储的双向链表
// 键值对:
//   HashMap<K, V>   :基于哈希表的无序键值对
//   BTreeMap<K, V>  :基于B树的有序键值对,按key排序
// 集合:
//   HashSet<T>      :基于哈希表的无序集合
//   BTreeSet<T>     :基于B树的有序集合
//   BinaryHeap<T>   :基于二叉堆的优先队列
use std::collections::VecDeque;
use std::collections::HashMap;


fn main() {
    // Vec创建方式-> Vec::new(), Vec::with_capacity(num), vec![]
    let mut v: Vec<u8> = Vec::new();
    // push()添加元素
    v.push(1);
    v.push(2);
    v.push(4);
    println!("{:?}", v);
    // 索引修改元素
    v[1] = 100;
    println!("{:?}", v);
    // 删除元素
    println!("e: {:?}", v.pop());
    println!("v: {:?}", v);
    println!("e: {:?}", v.remove(1));
    println!("v: {:?}", v);
    // 索引访问数组v[i]
    // get()访问数组v.get(i)
    // 遍历数组for i in v {}
    for value in v {
        println!("for: {}", value);
    }
    let vec = vec![10, 20 , 30];
    for value in vec {
        println!("for: {}", value);
    }

    // VecDeque创建方式-> VecDeque::new(), VecDeque::with_capacity(num)
    let mut vd: VecDeque<u32> = VecDeque::new();
    vd.push_back(1);
    vd.push_back(2);
    vd.push_back(3);
    vd.push_back(4);
    vd.push_back(5);
    vd.push_front(10);
    vd.push_front(20);
    vd.push_front(30);
    vd.push_front(40);
    vd.push_front(50);
    println!("vd: {:?}", vd);
    // 索引修改值
    vd[3] = 100;
    println!("vd: {:?}", vd);
    // 删除元素
    println!("e: {:?}", vd.pop_back());
    println!("e: {:?}", vd.pop_front());
    println!("vd: {:?}", vd);
    println!("e: {:?}", vd.remove(2));
    println!("vd: {:?}", vd);
    // 索引访问元素vd[i]
    // get访问元素vd.get(i)

    // HashMap-> HashMap::new(), HashMap::with_capacity(num)
    let mut m: HashMap<&str, i32> = HashMap::new();
    m.insert("zhangsan", 88);
    m.insert("wangwu", 66);
    println!("map: {:?}", m);
    // entry()检查键是否存在, or_insert()没有就插入值,否则不执行操作
    m.entry("zhuliu").or_insert(99);
    m.entry("lisu").or_insert(100);
    println!("{:?}", m);
    // 修改键对应的值
    for (_, v) in m.iter_mut() {
        *v += 2;
    }
    println!("map: {:?}", m);
    // remove()删除键值对
    m.remove("lisu");
    println!("map: {:?}", m);
    // 访问元素
    println!("zhangsan: {}", m["zhangsan"]);
    println!("zhangsan: {:?}", m.get("zhangsan"));
}
