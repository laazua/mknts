//程序控制

// if 条件控制
function ifTest(a) {
    if (a > 0) {
        console.log("a > 0");
    } else if (a < 0) {
        console.log("a < 0");
    } else {
        console.log("a == 0");
    }
}

// switch条件控制
function switchTest(grade) {
    switch (grade) {
        case 1:
            console.log("grade 1");
            break;
        case 2:
            console.log("grade 2");
            break;
        case 3:
            console.log("grade 3");
            break;
        default:
            console.log("not grade match!");
    }
}

// (条件)?表达式1:表达式2

// while循环
function whileTest(a) {
    while (a < 10) {
        a = a + 1;
        console.log("当前a的值为:", a)
    }
}

// for循环
function forTest(a) {
    for (let i = 0; i < a; i++) {
        console.log("当前i的值为:", i)
    }
}

// do...while循环
function doWhileTest(a) {
    let i = 0;
    let j = 5;
    do {
        console.log("当前i的值为:",i)
        i++;
    } while (i < j)
}

// break &&continue用于跳出循环

// 标签:label, 配合break && continue跳出特定循环
function labelTest() {
    for (let i = 0; i < 3; i++) {
        top:
        for (let j = 0; j < 5; j++) {
            if (i === 2 && j === 2) {
                break top;
            }
            console.log('i = ' + i + ', j = ' + j);
        }
    }
}