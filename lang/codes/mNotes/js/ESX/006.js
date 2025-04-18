// 箭头函数

let fun = (name) => {
    return `我是箭头函数${name}`;
};

// this是静态的,this始终指向函数声明所在的作用域
// 不能作为构造函数实例化对象
// 不能使用arguments变量
// 省略小括号(当形参有且只有一个时)
let plus = n => {
    return n + n;
};
// 省略花括号
let pow = n => n*n;
