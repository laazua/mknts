FROM python:3.10.7-slim-buster

WORKDIR /data

COPY ./ ./

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple\
    && pip config set install.trusted-host tuna.tsinghua.edu.cn \
    && pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 8888

CMD ["sh", "cmd.sh"]
