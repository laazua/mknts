FROM python:3.9.6-slim-buster

WORKDIR /app

COPY ./ ./

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 8888

CMD ["sh", "./cmd.sh"]