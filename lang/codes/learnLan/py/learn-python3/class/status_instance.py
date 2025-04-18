# -*- coding: uttf-8 -*-
"""
实现一个在不同状态下执行操作的对象,但是代码中有不想处想太多条件判断
"""


class Connection:
    """普通方案,好多个判断语句,效率低下"""

    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('already closed')
        self.state = 'CLOSED'


class ConnectionBetter:
    """新方案==对每个状态定义一个类"""

    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, new_state):
        self._state = new_state

    def read(self):
        return self._state.read(self)

    def write(self):
        return self._state.write(self)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


class ConnectionState:
    """connection state base class"""

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    """implementation of different states"""

    @staticmethod
    def read(conn):
        raise RuntimeError('ont open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('alrady closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)
