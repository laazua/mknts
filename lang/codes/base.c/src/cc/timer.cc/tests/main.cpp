#include "../src/timer.hpp"

int main() {
    TimeWheel timeWheel(1440); // 初始化一个大小为60的时间轮，每秒钟一个槽

    // 定义一个带参数的任务函数
    auto print_task = [](const string& message) {
        cout << "Task executed with message: " << message << endl;
    };

    // 设置一个任务，在指定的时间点执行打印函数
    auto exec_time = system_clock::time_point::min() + hours(9) + minutes(57) + seconds(0); // 2024-05-14 10:00:00
    Task task;
    task.exec_time = exec_time;
    task.task_func = bind(print_task, "Hello, World!");
    timeWheel.add_task(task);

    // 运行时间轮
    timeWheel.run();

    return 0;
}
