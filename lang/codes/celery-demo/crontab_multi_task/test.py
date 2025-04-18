import redis

rds = redis.Redis(host="127.0.0.1", port=6379, db=1)


for i in rds.lrange("_kombu.binding.celery", 0, -1):
    print(i)