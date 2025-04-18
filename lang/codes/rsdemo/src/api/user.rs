/// user api

// refer from crate root, or get some error
use crate::service::handle;
use crate::service::dao::user;


pub fn get_user() {
    println!("##### get user api #####");
    handle::handle_user();
    user::get_user_dao();
}