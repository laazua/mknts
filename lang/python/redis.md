### Redis

- **安装**
```bash
pip install "redis[hiredis]"
```

- **使用**
```python
import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# strings
r.set('language', 'Python')
print(r.get('language'))  # Output: Python

# hashes
r.hset('user:1000', 'name', 'Alice')
r.hset('user:1000', 'email', 'alice@example.com')
print(r.hgetall('user:1000'))
# Output: {'name': 'Alice', 'email': 'alice@example.com'}

# lists
r.rpush('tasks', 'task1')
r.rpush('tasks', 'task2')
print(r.lrange('tasks', 0, -1))
# Output: ['task1', 'task2']

# sets
r.sadd('tags', 'python')
r.sadd('tags', 'redis')
print(r.smembers('tags'))
# Output: {'python', 'redis'}

# sorted sets
r.zadd('leaderboard', {'Alice': 100, 'Bob': 95})
print(r.zrange('leaderboard', 0, -1, withscores=True))
# Output: [('Bob', 95.0), ('Alice', 100.0)]

# pipeline
pipe = r.pipeline()
pipe.set('foo', 'bar')
pipe.set('baz', 'qux')
pipe.execute()

# pub/sub
pubsub = r.pubsub()
pubsub.subscribe('channel1')
# In a separate thread or process
r.publish('channel1', 'Hello, Redis!')

# transactions
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch('balance')
            balance = int(pipe.get('balance'))
            if balance >= 50:
                pipe.multi()
                pipe.set('balance', balance - 50)
                pipe.execute()
                break
            else:
                pipe.unwatch()
                break
        except redis.WatchError:
            continue
```