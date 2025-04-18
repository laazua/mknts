/// this is a demo to learn rust's code organized


// refer from file mod route
// call file mod route.rs
mod route;
// refer from demo project name 
// call path mod api
use demo::api;


// project entry point
fn main() {
    // call route mod
    route::get_route();

    // call api mod
    api::user::get_user();
    api::role::get_role();
    api::menu::get_menu();
}
