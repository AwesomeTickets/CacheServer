FROM redis:3.2.9

WORKDIR /cache-server

COPY redis.conf /cache-server

EXPOSE 6379

CMD ["redis-server", "./redis.conf"]
