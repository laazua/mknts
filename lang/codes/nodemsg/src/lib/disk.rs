use std::thread;
use std::time::Duration;
use psutil::disk;

pub fn get_disk_msg(path: &str, second: u64) {
    let mut disk_io_counters_collector = disk::DiskIoCountersCollector::default();
    
    thread::sleep(Duration::from_millis(second));

    let disk_io_counters_per_partition = disk_io_counters_collector.disk_io_counters_per_partition().unwrap();
    let partitions = disk::partitions_physical().unwrap();
    let disk_usage = disk::disk_usage(path).unwrap();

    println!("disk io counters_per_patition: {:#?}", disk_io_counters_per_partition);
    println!("partitions: {:#?}", partitions);
    println!("disk_useage: {:#?}", disk_usage);
}