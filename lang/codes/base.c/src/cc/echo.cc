// echo.cc
#include "echo.hh"

// EchoServer 类的实现
EchoServer::EchoServer(boost::asio::io_context& io_context, short port)
    : io_context_(io_context), acceptor_(io_context, tcp::endpoint(tcp::v4(), port))
{
    startAccept();
}

void EchoServer::startAccept()
{
    // 创建一个新的 socket
    auto socket = std::make_shared<tcp::socket>(io_context_);

    // 异步等待连接
    acceptor_.async_accept(*socket, [this, socket](const boost::system::error_code& error) {
        handleAccept(socket, error);
    });
}

void EchoServer::handleAccept(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error)
{
    if (!error) {
        startRead(socket);
    }

    startAccept();
}

void EchoServer::startRead(std::shared_ptr<tcp::socket> socket)
{
    // 创建一个缓冲区
    auto buffer = std::make_shared<boost::asio::streambuf>();

    // 异步读取数据
    boost::asio::async_read_until(*socket, *buffer, '\n', [this, socket, buffer](const boost::system::error_code& error, size_t bytes_transferred) {
        handleRead(socket, error, buffer);
    });
}

void EchoServer::handleRead(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error, std::shared_ptr<boost::asio::streambuf> buffer)
{
    if (!error) {
        // 从缓冲区中读取消息
        std::istream is(buffer.get());
        std::string message;
        std::getline(is, message);

        // 回显消息给客户端
        startWrite(socket, message);
    }
}

void EchoServer::startWrite(std::shared_ptr<tcp::socket> socket, const std::string& message)
{
    // 异步写入数据
    boost::asio::async_write(*socket, boost::asio::buffer(message + "\n"), [this, socket](const boost::system::error_code& error, size_t bytes_transferred) {
        handleWrite(socket, error);
    });
}

void EchoServer::handleWrite(std::shared_ptr<tcp::socket> socket, const boost::system::error_code& error)
{
    // 不做任何操作，继续等待下一个消息
}
