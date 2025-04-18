/// menu api

// refer from crate root, or get some error
use crate::service::handle;
use crate::service::dao::menu;

pub fn get_menu() {
    println!("##### get menu api #####");
    handle::handle_menu();
    menu::get_menu_dao();
}