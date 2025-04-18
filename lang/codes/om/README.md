# vanGogh

* *description*
```
  - game deploy tool
  - master && worker architecture
  - communicate with http
  - features:
    1. zone: add, start, stop, reload, check
    2. zone: config && program update
    3. host: get info of host 
    ...
```

* *deployment*
```
  - deploy caller on master host:
    .-/
      /caller
      /config/caller.yaml

  - deploy slaver on slaver host:
    .-/
      /slaver
      /config/slaver.yaml

  - start one mongo db

  - modify config/caller.yaml, config/slaver.yaml
```