#include "echo.hh"
#include "chat.hh"
#include "proxy.hh"

int main() {
    /*   
    try {
        // 创建 Boost.Asio 的 io_context 对象
        boost::asio::io_context io_context;

        // 创建 EchoServer 对象并启动服务器，监听端口 8080
        EchoServer echo_server(io_context, 8080);

        // 运行异步事件循环
        io_context.run();
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    */

    /*
    try {
        boost::asio::io_service io_service;
        boost::asio::ip::tcp::endpoint endpoint(boost::asio::ip::tcp::v4(), 8080);
        ChatServer server(io_service, endpoint);
        io_service.run();
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    */

    return 0;
}

