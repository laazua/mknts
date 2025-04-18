// 迭代器

// 具备Iterator接口的对象都可以使用for...of遍历
// Array, Arguments, Set, Map, String, TypedArray, NodeList都具备Iterator

let names = ['zhangsan', 'lisi'];
for(let v of names){
    console.log(v);
}
