#include <iostream>
#include <memory>
#include <grpcpp/grpcpp.h>
#include "helloworld.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::ClientReader;
using grpc::Status;
using helloworld::Greeter;
using helloworld::HelloRequest;
using helloworld::HelloReply;

class GreeterClient {
public:
  GreeterClient(std::shared_ptr<Channel> channel)
      : stub_(Greeter::NewStub(channel)) {}

  // 1. 一元 RPC 调用
  std::string SayHello(const std::string& user) {
    HelloRequest request;
    request.set_name(user);
    HelloReply reply;
    ClientContext context;

    Status status = stub_->SayHello(&context, request, &reply);
    if (status.ok()) {
      return reply.message();
    } else {
      std::cerr << "RPC failed: " << status.error_code() << ": " << status.error_message() << std::endl;
      return "RPC failed";
    }
  }

  // 2. 服务端流式 RPC 调用
  void SayHelloStream(const std::string& user) {
    HelloRequest request;
    request.set_name(user);
    ClientContext context;

    auto reader = stub_->SayHelloStream(&context, request);
    HelloReply reply;
    while (reader->Read(&reply)) { // 循环读取流
      std::cout << "Stream: " << reply.message() << std::endl;
    }
    Status status = reader->Finish();
    if (!status.ok()) {
      std::cerr << "Stream RPC failed: " << status.error_message() << std::endl;
    }
  }

private:
  std::unique_ptr<Greeter::Stub> stub_;
};

int main() {
  // 连接服务器
  GreeterClient client(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));

  std::string user("World");
  std::string reply = client.SayHello(user);
  std::cout << "Unary RPC response: " << reply << std::endl;

  std::cout << "Server streaming RPC response:" << std::endl;
  client.SayHelloStream(user);

  return 0;
}
