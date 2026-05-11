#include <iostream>
#include <memory>
#include <grpcpp/grpcpp.h>
#include "helloworld.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::ServerWriter;
using grpc::Status;
using helloworld::Greeter;
using helloworld::HelloRequest;
using helloworld::HelloReply;

// 1. 继承生成的抽象服务类
class GreeterServiceImpl final : public Greeter::Service {
  
  // 2. 重写一元 RPC 方法
  Status SayHello(ServerContext* context, const HelloRequest* request,
                  HelloReply* reply) override {
    std::string prefix("Hello ");
    reply->set_message(prefix + request->name());
    return Status::OK;
  }

  // 3. 重写服务端流式 RPC 方法
  Status SayHelloStream(ServerContext* context, const HelloRequest* request,
                        ServerWriter<HelloReply>* writer) override {
    HelloReply reply;
    // 连续发送 5 条消息
    for (int i = 1; i <= 5; ++i) {
      reply.set_message("Hello " + request->name() + " [" + std::to_string(i) + "]");
      writer->Write(reply);
    }
    return Status::OK;
  }
};

int main() {
  std::string server_address("0.0.0.0:50051");
  GreeterServiceImpl service;

  // 4. 构建并启动服务器
  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());

  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait(); // 阻塞直到服务器关闭
  return 0;
}
