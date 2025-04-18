from abc import ABC, abstractmethod


class FileManager(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class LocalFileManager(FileManager):
    def read(self):
        print("Reading from local file")

    def write(self, data):
        print("Writing to local file:", data)


class RemoteFileManager(FileManager):
    def read(self):
        print("Reading from remote file")

    def write(self, data):
        print("Writing to remote file:", data)


# 函数接受任何具有 read() 和 write() 方法的对象
def operate_file(file_manager):
    file_manager.read()
    file_manager.write("Hello, World!")


# 创建不同的文件管理器对象
local_file_manager = LocalFileManager()
remote_file_manager = RemoteFileManager()

# 调用函数，传入不同的文件管理器对象
operate_file(
    local_file_manager
)  # 输出: Reading from local file Writing to local file: Hello, World!
operate_file(
    remote_file_manager
)  # 输出: Reading from remote file Writing to remote file: Hello, World!
