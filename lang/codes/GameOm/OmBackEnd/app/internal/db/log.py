from . import Log, MonDb


class LogDb(MonDb):
    def __init__(self) -> None:
        super(LogDb, self).__init__()

    def add(self, name: str = None, action: str = None) -> bool:
        try:
            log = Log(
                name = name,
                action = action
            )
            log.save()
            return True
        except Exception as e:
            print('add log failed: ', e)
            return False

    def get(self, name) -> list:
        try:
            return [ {'name': log.name, 'action': log.action, 'ctime': log.create_time} for log in Log.objects(name=name) ]
        except Exception as e:
            print('get log failed: ', e)
            return None


log_db = LogDb()
