FROM python:3.10.14-alpine3.20

COPY .env taoist-0.0.1-py3-none-any.whl .


RUN sed -i 's/https:\/\/dl-cdn.alpinelinux.org/https:\/\/mirrors.tuna.tsinghua.edu.cn/' /etc/apk/repositories && \
    apk update && \
    apk add pkgconf build-base mariadb-dev mysql-dev  && \
    pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  && \
    pip install taoist-0.0.1-py3-none-any.whl -i https://pypi.tuna.tsinghua.edu.cn/simple 


EXPOSE 7000

CMD ["taoist"]
