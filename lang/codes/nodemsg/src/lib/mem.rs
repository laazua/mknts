use psutil::memory;

pub fn get_mem_msg() {
    let vritual_memory = memory::virtual_memory().unwrap();
    let swap_memory = memory::swap_memory().unwrap();

    println!("virtual memory: {:#?}", vritual_memory);
    println!("swap memory: {:#?}", swap_memory);
}