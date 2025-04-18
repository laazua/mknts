#include "storage.hpp"


Storage::Storage(const std::string& filename):
  filename(filename)
{
  load_from_file();
}

void Storage::load_from_file()
{
  std::ifstream file(filename);
  if (file.is_open()) {
    std::string line;
    while (std::getline(file, line)) {
      size_t pos = line.find('=');
      if (pos != std::string::npos) {
        std::string key = line.substr(0, pos);
        std::string value = line.substr(pos + 1);
        data[key] = value;
      }
      file.close();
    }
  }
}

void Storage::save_to_file()
{
  std::ofstream file(filename);
  if (file.is_open()) {
    for (const auto& pair : data) {
      file << pair.first << "=" << pair.second << std::endl;
    }
    file.close();
  }
}

void Storage::set(const std::string& key, const std::string& value)
{
  load_from_file();
  data[key] = value;
  save_to_file();
}

std::string Storage::get(const std::string& key)
{
  if (data.find(key) != data.end()) {
    return data[key];
  }
  return "";
}

void Storage::del(const std::string& key)
{
  load_from_file();
  if (data.find(key) != data.end()) {
    data.erase(key);
    save_to_file(); 
  }
}
