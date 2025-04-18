
from abc import ABCMeta, abstractmethod


class Zone(metaclass=ABCMeta):
    @abstractmethod
    def zone_open(self, data):
        pass

    @abstractmethod
    def zone_start(self, data):
        pass

    @abstractmethod
    def zone_stop(self, data):
        pass

    @abstractmethod
    def zone_svn_update(self, data):
        pass

    @abstractmethod
    def zone_bin_update(self, data):
        pass


class Resource(metaclass=ABCMeta):
    @abstractmethod
    def svn_update(self, data):
        pass

    @abstractmethod
    def bin_update(self, data):
        pass