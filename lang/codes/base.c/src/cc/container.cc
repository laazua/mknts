#include <map>
#include <set>
#include <list>
#include <stack>
#include <array>
#include <deque>
#include <queue>
#include <array>
#include <vector>
#include <string>
#include <iostream>

int main()
{
    // 数组
    std::cout << "##### array #####" << std::endl;
    std::array<int, 5> arra = {100, 23, 49, 56, 73};
    for (auto item = arra.begin(); item != arra.end(); item++)
        std::cout << *item << std::endl;

    // 双端队列
    std::cout << "##### deque #####" << std::endl;
    std::deque<int> dq;
    for (int idx=0; idx<5; idx++) dq.push_back(idx);

    std::deque<int>::iterator item = dq.begin();
    while (item != dq.end()) std::cout << *item++ << std::endl;

    // 列表
    std::cout << "##### list #####" << std::endl;
    int arrs[] = {21, 43, 56, 52, 23};
    std::list<int> arr(arrs, arrs + 5);
    for (std::list<int>::iterator item = arr.begin(); item != arr.end(); item++)
        std::cout << *item << std::endl;

    // map
    std::cout << "###### map ######" << std::endl;
    std::map<std::string, std::string> dict;
    dict[std::string("name")] = std::string("zhangsan");
    dict[std::string("addr")] = std::string("chengdushi");
    for (auto item = dict.begin(); item != dict.end(); item++)
        std::cout << item->first << ": " << item->second << std::endl;

    // multi map
    std::cout << "### multi map ###" << std::endl;
    std::multimap<std::string, std::string> mdict;
    mdict.insert(std::pair<std::string, std::string>("name", "lisi"));
    mdict.insert(std::pair<std::string, std::string>("addr", "beijingshi"));
    for (auto item = mdict.begin(); item != mdict.end(); item++)
        std::cout << (*item).first << ": " << (*item).second << std::endl;

    // queue
    std::cout << "##### queue #####" << std::endl;
    std::queue<std::string> queue;
    queue.push("apple");
    queue.push("bnana");
    queue.push("orange");
    std::cout << "queue size: " << queue.size() << std::endl;

    // set
    std::cout << "###### set ######" << std::endl;
    int msets[] = {12, 34, 54, 12, 67, 78};
    std::set<int> mset(msets, msets + 6);
    for (auto item = mset.begin(); item != mset.end(); item++)
        std::cout << *item << std::endl;  

    // multi set
    std::cout << "### multi set ###" << std::endl;
    int mmsets[] = {23, 67, 67, 67, 78, 89, 100};
    std::multiset<int> mmset(mmsets, mmsets + 7);
    for (auto item = mmset.begin(); item != mmset.end(); item++)
        std::cout << *item << std::endl;

    // stack
    std::cout << "##### stack #####" << std::endl;
    std::stack<int> stack;
    stack.push(12);
    stack.push(45);
    stack.push(78);
    std::cout << "stack size: " << stack.size() << std::endl;

    // vector
    std::cout << "##### vector #####" << std::endl;
    std::vector<int> vec;
    for (int idx=0; idx<5; idx++) vec.push_back(idx);
    for (auto item = vec.begin(); item != vec.end(); item++)
        std::cout << *item << std::endl;

    return 0;
}
// 输出
// ##### array #####
// 100
// 23
// 49
// 56
// 73
// ##### deque #####
// 0
// 1
// 2
// 3
// 4
// ##### list #####
// 21
// 43
// 56
// 52
// 23
// ###### map ######
// addr: chengdushi
// name: zhangsan
// ### multi map ###
// addr: beijingshi
// name: lisi
// ##### queue #####
// queue size: 3
// ###### set ######
// 12
// 34
// 54
// 67
// 78
// ### multi set ###
// 23
// 67
// 67
// 67
// 78
// 89
// 100
// ##### stack #####
// stack size: 3
// ##### vector #####
// 0
// 1
// 2
// 3
// 4

