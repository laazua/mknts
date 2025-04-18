use psutil::host;

pub fn get_load_msg() {
    let loadavg = host::loadavg().unwrap();
    println!("loadavg: {:#?}", loadavg);
}