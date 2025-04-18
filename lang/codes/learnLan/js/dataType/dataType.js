// 基本数据类型

function dataType() {
    let a = null    // 零值
    let b = undefined    // NaN

    let isTrue = true    // 真
    let isFalse = false    // 假
    // undefined, null, 0, NaN, "", '' 都将转换为false,其余转换为true
    // 空数组([])和空对象({})对应的布尔值为true

    // numbers
    let num_1 = 1
    let num_2 = 1.0
    // num_1 === num_2  // true
    // JavaScript 语言的底层根本没有整数, 所有数字都是小数（64位浮点数）
    // 由于浮点数不是精确的值,所以涉及小数的比较和运算要特别小心
    
    // parseInt(), parseFloat()
    // isNaN()
    // isFinite()
    
    // string
    let str_1 = 'abc'
    let str_2 = "abc"
    // str_1[0] === str_2[0]  true
    // str_1.length  3
}

// 编码
function b64EnCode(str) {
    return btoa(encodeURIComponent(str))
}

// 解码
function b64DeCode(str) {
    return decodeURIComponent(atob(str))
}

// 对象,当不同对象指向同一个对象时,则这些变量指向同一块内存地址
var obj = {
    foo: "haha",
    bar: "hehe",
    p: function(x) {
           return x + 2;
    },
    // tar属性指向一个对象,形成了链式引用
    tar: {
        name: "bobo",
        age: 12
    }
};

{ bar: 123 }    // 语句块
({ bar: 123 })    // 对象

// 函数
function print(s) {
    console.log(s);
}

var print = function(s) {
    console.log(s)
}

// 立即调用函数,必须分号结尾
(function(){/*code*/});


// 数组
var arr = [1, 'a', [1, 2, 3]]
arr.length    // 3