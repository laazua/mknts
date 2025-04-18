#ifndef ECHO_SERVER_H
#define ECHO_SERVER_H

#include <iostream>
#include <memory>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

// EchoServer 类的声明
class EchoServer
{
public:
    // 构造函数
    EchoServer(boost::asio::io_context& io_context, short port);

private:
    // 处理新连接
    void startAccept();

    // 处理已连接的客户端
    void handleAccept(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error);

    // 处理客户端发送的消息
    void startRead(std::shared_ptr<tcp::socket> socket);

    // 处理读取完成的消息
    void handleRead(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error, std::shared_ptr<boost::asio::streambuf> buffer);

    // 处理写操作
    void startWrite(std::shared_ptr<tcp::socket> socket, const std::string& message);

    // 处理写完成
    void handleWrite(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error);

    // Boost.Asio 的 io_context 对象
    boost::asio::io_context& io_context_;

    // 监听的端口号
    tcp::acceptor acceptor_;
};

#endif // ECHO_SERVER_H

