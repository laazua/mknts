FROM python:3.10.7-slim-buster

WORKDIR /data

COPY ./ ./

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 8887

CMD ["python", "main.py"]