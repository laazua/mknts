FROM python:3.10.2-slim-buster

WORKDIR /data

COPY ./ ./

RUN python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 9888

CMD [ "python", "app/main.py" ]