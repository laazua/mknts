
fn main() {
    let ben_zi = mlib::car::BenZi{name: String::from("ben_zi")};
    let bao_ma = mlib::car::BaoMa{name: String::from("bao_ma")};
    mlib::car::run_car(ben_zi);
    mlib::car::run_car(bao_ma);

    let apple = mlib::fruit::fruit::Apple;
    let banana = mlib::fruit::fruit::Banana;
    mlib::fruit::fruit::show_fruit(apple);
    mlib::fruit::fruit::show_fruit(banana);
}
