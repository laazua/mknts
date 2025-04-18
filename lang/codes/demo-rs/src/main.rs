use chat;
use echo;
use proxy;

fn main() {
    echo::start_server();
    chat::start_server();
    proxy::start_server();
}
