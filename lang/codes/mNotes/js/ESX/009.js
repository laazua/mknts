// js的第七种数据类型
// symbol的值唯一,解决命名冲突
// symbol不能与其它数据进行运算
// symbol定义的对象不能使用for...in遍历,可以使用Reflect.ownKeys来获取对象的所有键名

let s1 = Symbol();
let s2 = Symbol('abc');
