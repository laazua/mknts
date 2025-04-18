#ifndef _STORAGE_H_
#define _STORAGE_H_

#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

class Storage
{
private:
  std::string filename;
  std::unordered_map<std::string, std::string> data;

  void load_from_file();
  void save_to_file();
public:
  Storage(const std::string& filename);
  void set(const std::string& key, const std::string& value);
  std::string get(const std::string& key);
  void del(const std::string& key);
};

#endif // _STORAGE_H_
