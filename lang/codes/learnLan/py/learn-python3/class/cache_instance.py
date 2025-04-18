# -*- coding: utf-8 -*_
"""
缓存实例
"""
import weakref


class Spam:
    def __init__(self, name):
        self.name = name


# caching support
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]

    return s


class CachedSpamManager:
    """高级的实例缓存"""

    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]

        return s

    def clear(self):
        self._cache.clear()


class Spam:

    def __init__(self, *args, **kwargs):
        raise RuntimeError('can not instantiate directly')

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


if __name__ == '__main__':
    a = get_spam('aa')
    b = get_spam('bb')
    print(a is b)

    c = get_spam('aa')
    print(a is c)
