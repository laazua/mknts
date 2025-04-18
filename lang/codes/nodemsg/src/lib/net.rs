use std::thread;
use std::time::Duration;
use psutil::network;


pub fn get_net_msg(second: u64) {
    let mut net_io_counters_collector = network::NetIoCountersCollector::default();

    thread::sleep(Duration::from_millis(second));

    let net_io_counters = net_io_counters_collector.net_io_counters().unwrap();

    println!("net io counters: {:#?}", net_io_counters);
}