#ifndef _TIME_WHEEL_
#define _TIME_WHEEL_

#include <iostream>
#include <chrono>
#include <functional>
#include <thread>
#include <vector>
#include <algorithm>

using namespace std;
using namespace std::chrono;

// 定义任务结构体，包含执行时间和任务函数
struct Task {
  function<void()> task_func;
  system_clock::time_point exec_time;
};

class TimeWheel
{
public:
  TimeWheel(int size);
  void add_task(const Task& task);
  void run();
private:
  int size; // 时间轮的大小
  int current_slot; // 当前指针指向的槽
  vector<vector<Task>> slots; // 时间轮的槽，每个槽包含一个任务链表
  // 执行任务槽中的任务
  void exec_task(int slot);
};

#endif // _TIME_WHEEL_

