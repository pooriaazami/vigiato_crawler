import redis


class RedisInterface:

    def __init__(self):
        self.__host = 'localhost'
        self.__port = 6379
        self.__password = ''

        self.__connection = redis.StrictRedis(
            host=self.__host,
            port=self.__port,
            password=self.__password
        )

        self.__set_name = 'links'

    def add_item(self, item):
        return self.__connection.sadd(self.__set_name, item)
