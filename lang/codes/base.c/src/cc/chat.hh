// chat.hh

#ifndef CHAT_SERVER_H
#define CHAT_SERVER_H

#include <iostream>
#include <memory>
#include <set>
#include <boost/asio.hpp>

class ChatSession : public std::enable_shared_from_this<ChatSession>
{
public:
    ChatSession(boost::asio::ip::tcp::socket socket, std::set<std::shared_ptr<ChatSession>>& sessions);

    void start();

    void deliver(const std::string& msg);

private:
    void readMessage();
    void handleRead(const boost::system::error_code& error, std::size_t bytes_transferred);
    void handleWrite(const boost::system::error_code& error);

    boost::asio::ip::tcp::socket m_socket;
    std::set<std::shared_ptr<ChatSession>>& m_sessions;
    boost::asio::streambuf m_buffer; // Modified: Using streambuf for buffer
    std::string m_message;
};

class ChatServer
{
public:
    ChatServer(boost::asio::io_service& io_service, const boost::asio::ip::tcp::endpoint& endpoint);

private:
    void acceptConnection();
    void handleAccept(const boost::system::error_code& error);

    boost::asio::ip::tcp::acceptor m_acceptor;
    boost::asio::ip::tcp::socket m_socket;
    std::set<std::shared_ptr<ChatSession>> m_sessions;
};

#endif // CHAT_SERVER_H

