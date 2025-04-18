#include "timer.hpp"

TimeWheel::TimeWheel(int size): 
  size(size), current_slot(0)
{
  slots.resize(size);
}

// 添加任务到时间轮
void TimeWheel::add_task(const Task& task) {
  auto exec_time = task.exec_time;
  auto now = system_clock::now();
  auto duration = duration_cast<seconds>(exec_time - now);
  int offset = duration.count() % size;
  slots[(current_slot + offset) % size].push_back(task);
}

// 运行时间轮，检查是否有任务到期
void TimeWheel::run() {
  while (true) {
    auto now = system_clock::now();
    int now_slot = duration_cast<seconds>(now.time_since_epoch()).count() % size;
    if (now_slot != current_slot) {
      exec_task(current_slot);
      current_slot = now_slot;
    }
    this_thread::sleep_for(seconds(1440)); // 时间轮的时间间隔
  }
}

// 执行当前槽中的任务
void TimeWheel::exec_task(int slot) {
  for (const auto& task : slots[slot]) task.task_func();
  slots[slot].clear();
}
