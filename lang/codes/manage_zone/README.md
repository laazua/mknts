### manage zone

* **description**
```
  - A web application for managing game servers
  - Main components used: fastapi, mongoEngine, fabric
  - The main node and sub-nodes depend on sshd, 
    so the main node and sub-nodes establish a login-free relationship through the common user gamecpp (or other user names you like), 
    and all operations of the main node to the sub-nodes are done through the gamecpp user
```

* **app start**
```
  - Create a virtual environment
    mkdir appPath && cd appPath && pipenv --python 3.9 && pipenv install -r requirements.txt
  - Start the app
    sh manage.sh start
```

* **reference**
```
  - mongoEngine
    http://docs.mongoengine.org/tutorial.html
```
