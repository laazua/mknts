/// rust app 


// use std::path::Path;
use  clap::{App, Arg};

mod lib;

fn main() {
    let matches = App::new("nodemsg")
        .version("0.0.1")
        .author("Sseve")
        .about("print node message")
        .arg(Arg::with_name("cpu")
            .short("c")
            .long("cpu")
            .multiple(true)
            .help("print cpu message"))
        .arg(Arg::with_name("disk")
            .short("d")
            .long("disk")
            .multiple(true)
            .help("print disk message"))
        .arg(Arg::with_name("load")
            .short("l")
            .long("load")
            .multiple(true)
            .help("print load message"))
        .arg(Arg::with_name("mem")
            .short("m")
            .long("mem")
            .multiple(true)
            .help("print mem message"))
        .arg(Arg::with_name("net")
            .short("n")
            .long("net")
            .multiple(true)
            .help("print net message"))
        .arg_from_usage("-p, --path=[PATH] 'the path of disk mount, and use with disk flag'")
        .arg_from_usage("-s, --second=[second] 'the second scop which used to cpu and net flag'")
        .get_matches();

    if matches.is_present("cpu") {
        if let Some(second) =  matches.value_of("second") {
            let sec = second.parse::<u64>().unwrap();
            lib::cpu::get_cpu_msg(sec*1000);
        } else {
            println!("if you want get cpu info, please: nodemsg -c -s 1");
        }
    } else if matches.is_present("disk") {
        if let Some(path) = matches.value_of("path") {
            if let Some(second) = matches.value_of("second"){
                let sec = second.parse::<u64>().unwrap();
                lib::disk::get_disk_msg(path, sec*1000);
            } else {
                println!("if you want get disk info, please: nodemsg -d -p '/run' -s 1");
            }
        } else {
            println!("if you want get disk info, please: nodemsg -d -p '/run' -s 1");
        }
        
    } else if matches.is_present("load") {
        lib::load::get_load_msg();
    } else if matches.is_present("mem") {
        lib::mem::get_mem_msg();
    } else if matches.is_present("net") {
        if let Some(second) =  matches.value_of("second") {
            let sec = second.parse::<u64>().unwrap();
            lib::net::get_net_msg(sec*1000)
        } else {
            println!("if you want get net info, please: nodemsg -n -s 1");
        }
    } else {
        println!("run: nodemsg -h for help.")
    }
}
