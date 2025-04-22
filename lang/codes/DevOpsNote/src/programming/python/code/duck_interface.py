# class FileManager:
#     def read(self):
#         raise NotImplementedError

#     def write(self, data):
#         raise NotImplementedError


class LocalFileManager:
    def read(self):
        print("Reading from local file")

    def write(self, data):
        print("Writing to local file:", data)


class RemoteFileManager:
    def read(self):
        print("Reading from remote file")

    def write(self, data):
        print("Writing to remote file:", data)


# 函数接受任何实现了 read() 和 write() 方法的对象
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
