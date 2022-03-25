#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
# coding=utf-8
import cgi
import cgitb
import json
import sys
import os
from http import cookies

print("Content-type:text/html")
print()


# TODO 获取cookie的方式
def get_cookie():
    """
    取出浏览器中的name为session_id的cookie数据
    :return:
    """
    if 'HTTP_COOKIE' in os.environ:
        cookie_string = os.environ.get('HTTP_COOKIE')
        c = cookies.SimpleCookie()
        c.load(cookie_string)
        data = None
        # print(c)
        try:
            data = c['session_id'].value
        except KeyError:
            data = None
    return data


if __name__ == '__main__':
    print(get_cookie())