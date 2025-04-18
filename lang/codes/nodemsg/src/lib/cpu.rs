use std::time::Duration;
use std::thread;
use psutil::cpu;


pub fn get_cpu_msg(msecond: u64) {
    let block_time = Duration::from_millis(msecond);  
    
    let mut cpu_percent_collector = cpu::CpuPercentCollector::new().unwrap();
    let mut cpu_times_percent_collector = cpu::CpuTimesPercentCollector::new().unwrap();
    
    thread::sleep(block_time);

    let cpu_percents_percpu = cpu_percent_collector.cpu_percent_percpu().unwrap();
    let cpu_times_percpu = cpu::cpu_times_percpu().unwrap();
    let cpu_times_percent_percpu = cpu_times_percent_collector.cpu_times_percent_percpu().unwrap();

    println!("cpu percent: {:#?}", cpu_percents_percpu);
    println!("cpu time percent: {:#?}", cpu_times_percpu);
    println!("cpu per time percent: {:#?}", cpu_times_percent_percpu);
}