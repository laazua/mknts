#include "../src/storage.hpp"

const std::string Usage = 
"Usage: storage -set key value \n"
"       storage -get key \n"
"       storage -del key \n";

int main(int argc, const char *argv[])
{
  Storage storage("data.txt");

  // storage.set("name", "zhangsan");
  // storage.set("addr", "beijing");

  // std::cout << "Name: " << storage.get("name") << std::endl;
  // std::cout << "Addr: " << storage.get("addr") << std::endl;
  // storage.del("addr");
  if (argc < 2) {
    std::cout << Usage << std::endl;
    return -1;
  }
  
  if (argv[1] == std::string("-set")) {
    storage.set(argv[2], argv[3]);
  } else if (argv[1] == std::string("-get")) {
    storage.get(argv[2]);
  } else if (argv[1] == std::string("-del")) {
    storage.del(argv[2]);
  } else {
    std::cout << Usage << std::endl;
  }

  return 0;
}
