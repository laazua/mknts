FROM python:3.10.13-slim-bullseye

WORKDIR /app/hiflask

COPY src .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8889

CMD ["python", "-m", "src.hiflask"]