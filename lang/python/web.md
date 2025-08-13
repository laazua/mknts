### web

- **django**
1. 开发时,创建项目:
   > mkdir ProjectName  
   > cd ProjectName  
   > python -m venv .venv  
   > source .venv/bin/activate  
   > python -m pip install django  
   > django-admin startproject ProjectName .  

2. 推荐在项目根目录下创建apps目录来创建应用模块
   > mkdir apps && cd apps
   > django-admin startapp AppName

- **项目示例**
```bash
## 项目为: v2api
## tree -I '.*' v2api

v2api/
├── apps
│   └── user
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── manage.py
└── v2api
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
