# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:38:03 2017

@author: admin
"""

import functools
def Handler_decorator(path,*,method):
    def decorator(func):
        @functools.wraps(func)#更正函数签名
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__route__ = path #存储路径信息,注意这里属性名叫route
        wrapper.__method__ = method #存储方法信息
        return wrapper
    return decorator

get = functools.partial(Handler_decorator,method = 'GET')
post = functools.partial(Handler_decorator,method = 'POST')