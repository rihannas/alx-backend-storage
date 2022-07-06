#!/usr/bin/env python3
""" Module for Redis db """

import redis
from uuid import uuid4
from typing import Union

"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
named _redis (using redis.Redis())
and flush the instance using flushdb.
Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the key.
Type-annotate store correctly.
Remember that data can be a str, bytes, int or float.
"""


class Cache:
    """classfor operating caching systems"""

    def __init__(self):
        """Instance for redis db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and
        return the key.
        """

        key = str(uuid4())
        self._redis.mset({key: data})

        return key
