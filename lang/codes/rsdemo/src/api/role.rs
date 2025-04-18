/// role api

// refer from crate root, or get some error
use crate::service::handle;
use crate::service::dao::role;


pub fn get_role() {
    println!("##### get role api #####");
    handle::handle_role();
    role::get_role_dao();
}