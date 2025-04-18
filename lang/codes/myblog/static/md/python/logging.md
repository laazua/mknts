## ***logging模块***

* *说明*
* > logging模块包含4个主要对象:
```
    - logger，是程序信息输出的主要接口，他分散在不同的代码中，使得程序可以在运行的时候记录响应的信息，并根据设置的日志级别或filter来决定哪些信息需要输出，并将这些信息分发到其它的关联的handler。
      常用的方法有：logger.setLevel(), logger.addHandler(), logger.removeHandler(), logger.addFilter(), logger.debug(), logger.info(), logger.warning(), logger.error(), etLogger()等。
    - handler， 用来处理信息的输出。可以将信息输出到控制台，文件或者网络。可以通过logger.addHandler()来给logger对象添加handler，常用的handler有StreamHandler和FilterHandler类。StreamHandler发
      送错误信息到流，FilterHandler类用于向文件输出日志信息，这两个handler在logging的核心模块中，其它的handler定义在logging.handles模块中，如HTTPHandler，SocketHandler。
    - formatter，决定log信息的格式。
    - Filter，用来决定哪些信息需要输出。可以被handler和logger使用。
```

* *示例*
```
import loggin


logging.basicConfig(
    level=logging.DEBUG,
    filename='log.txt',
    filemode='w',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)
logger = logging.getLogger(__name__)


logger.debug("[DEBUG]: message")
logger.info("[INFO]: message)
```