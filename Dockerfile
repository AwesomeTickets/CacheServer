FROM redis:3.2.9

WORKDIR /app
ADD redis.conf /app

CMD ["redis-server", "./redis.conf"]
