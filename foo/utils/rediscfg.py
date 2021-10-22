import redis

r = redis.StrictRedis(host='146.56.199.55', port=6379, password='wei%123456', decode_responses=True)
# r.set('first', 1)
# r.set('first', 2)
# r.setex('first', 3, 4)
print(r.get('first'))
