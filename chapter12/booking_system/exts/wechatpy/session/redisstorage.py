# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from exts.wechatpy.session import SessionStorage
from exts.wechatpy.utils import to_text
from exts.wechatpy.utils import json


class RedisStorage(SessionStorage):

    def __init__(self, redis, prefix="wechatpy"):
        for method_name in ("get", "set", "delete"):
            assert hasattr(redis, method_name)
        self.redis = redis
        self.prefix = prefix

    def key_name(self, key):
        return "{0}:{1}".format(self.prefix, key)

    def get(self, key, default=None):
        key = self.key_name(key)
        value = self.redis.get(key)
        if value is None:
            return default
        return json.loads(to_text(value))

    def set(self, key, value, ttl=None):
        if value is None:
            return
        key = self.key_name(key)
        value = json.dumps(value)
        self.redis.set(key, value, ex=ttl)

    def delete(self, key):
        key = self.key_name(key)
        self.redis.delete(key)
