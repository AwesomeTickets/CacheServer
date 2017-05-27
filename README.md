# CacheServer

Server that uses redis as cache.

## Installation

- Requirements

    - redis 3.2.9

- Run locally

    ```bash
    $ redis-server ./redis.conf
    ```

- Run with docker

    ```bash
    $ docker build -t cache-server .
    $ docker run --name cache-server -p 6379:6379 -d cache-server
    ```

## License

See the [LICENSE](./LICENSE) file for license rights and limitations.
