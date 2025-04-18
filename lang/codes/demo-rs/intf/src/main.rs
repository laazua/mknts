
fn main() {
    // 面向接口
    let circle = mlib::shape::Circle{ radius: 5.2 };
    let rectangle = mlib::shape::Rectangle{width: 2.3, height: 3.4};
    mlib::shape::shape_info(&circle);
    mlib::shape::shape_info(&rectangle);

    // 依赖注入
    // 使用 ConsoleLogger
    let console_logger = Box::new(mlib::log::ConsoleLog) as Box<dyn mlib::log::Logger>;
    let app_one = mlib::log::App::new(console_logger);
    app_one.run();

    // 使用 FileLogger
    let file_logger = Box::new(mlib::log::FileLog { path: String::from("app.log") }) as Box<dyn mlib::log::Logger>;
    let app_tow = mlib::log::App::new(file_logger);
    app_tow.run();
}
