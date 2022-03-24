#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
import secrets
import cgi
import datetime
import os
import json
import cgitb
from http import cookies
from mysql import query_data, insert_or_update_data, exist_db, exist_tb_in_db, DBNAME
cgitb.enable()

print("Content-type:application/json")
print()

# 获取用户名和密码
form = cgi.FieldStorage()
name_front = form.getvalue("name")
pwd_front = form.getvalue("pwd")


sql = 'select user_name,pwd from User where user_name = \"{}\"'.format(name_front)
res = query_data(sql)
if len(res) == 0:
    result = {"status_code": 0,
              "status_str": "login failed, the user is not registered, please register firstly."
              }
elif res[0]['pwd'] != pwd_front:
    result = {"status_code": 1,
              "status_str": "login failed, wrong password, please login again. "
              }
else:
    result = {"status_code": 2,
              "status_str": "login successfully "
              }
print(json.dumps(result))

    # TODO 服务器生成session_id 以及expire_time
    # session_id = secrets.token_urlsafe(16)
    # session_id = "555444666111"
    # GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    # expire_time = (datetime.datetime.now() + datetime.timedelta(hours=+1)).strftime(GMT_FORMAT)

    # print('Set-Cookie: session_id={}; expires={}'.format(session_id, expire_time))
    # TODO 将session_id写入cookie，将expire_time作为cookie的有效时间
    # TODO 浏览器的每次访问都会自动加上cookie用以验证，直到cookie失效
    # print("login successfully")


# TODO 获取cookie的方式
# if 'HTTP_COOKIE' in os.environ:
#     cookie_string = os.environ.get('HTTP_COOKIE')
#     c = cookies.SimpleCookie()
#     c.load(cookie_string)
#     print(c)
#     try:
#         data = c['session_id'].value
#         print("cookie data: " + data + "<br>")
#     except KeyError:
#         print("cookie 没有设置或者已过期<br>")
