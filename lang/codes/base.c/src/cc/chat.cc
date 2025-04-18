// chat.cc

#include "chat.hh"

using namespace boost::asio;
using namespace boost::asio::ip;
using namespace std;

ChatSession::ChatSession(tcp::socket socket, set<shared_ptr<ChatSession>>& sessions)
    : m_socket(std::move(socket)), m_sessions(sessions) {}

void ChatSession::start()
{
    m_sessions.insert(shared_from_this());
    readMessage();
}

void ChatSession::readMessage()
{
    async_read_until(m_socket, m_buffer, '\n', // Modified: Using m_buffer
        [self = shared_from_this()](const boost::system::error_code& error, size_t bytes_transferred) {
            if (!error) {
                istream is(&self->m_buffer);
                std::getline(is, self->m_message);
                self->deliver(self->m_message);
                self->readMessage();
            } else {
                self->m_sessions.erase(self);
            }
        });
}

void ChatSession::deliver(const string& msg)
{
    for (auto& session : m_sessions) {
        async_write(session->m_socket, buffer(msg + "\n"), [](const boost::system::error_code& /*error*/, size_t /*bytes_transferred*/) {});
    }
}

ChatServer::ChatServer(io_service& io_service, const tcp::endpoint& endpoint)
    : m_acceptor(io_service, endpoint), m_socket(io_service) 
{
    acceptConnection();
}

void ChatServer::acceptConnection()
{
    m_acceptor.async_accept(m_socket,
        [this](const boost::system::error_code& error) {
            if (!error) {
                make_shared<ChatSession>(std::move(m_socket), m_sessions)->start();
            }
            acceptConnection();
        });
}

void ChatServer::handleAccept(const boost::system::error_code& error)
{
    if (!error) {
        make_shared<ChatSession>(std::move(m_socket), m_sessions)->start();
    }
    acceptConnection();
}

