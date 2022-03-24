import os
from http import cookies


def get_cookie(name):
    """
    取出浏览器中的名为name的cookie数据
    :return:
    """
    if 'HTTP_COOKIE' in os.environ:
        cookie_string = os.environ.get('HTTP_COOKIE')
        c = cookies.SimpleCookie()
        c.load(cookie_string)
        try:
            data = c[name].value
            print("cookie data: " + data + "<br>")
        except KeyError:
            print("cookie Not set or expired <br>")
    return data
