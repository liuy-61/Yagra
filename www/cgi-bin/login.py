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


# 获取用户名和密码
form = cgi.FieldStorage()
name_front = form.getvalue("name")
pwd_front = form.getvalue("pwd")


sql = 'select user_name,pwd from User where user_name = \"{}\"'.format(
    name_front)
res = query_data(sql)
if len(res) == 0:
    result = {
        "status_code": 0,
        "status_str": "login failed, the user is not registered, please register firstly."}
elif res[0]['pwd'] != pwd_front:
    result = {
        "status_code": 1,
        "status_str": "login failed, wrong password, please login again. "}
else:
    result = {"status_code": 2,
              "status_str": "login successfully "
              }
print("Content-type:text/html")

# 如果登录成功,服务器生成session_id,以及expire_time,同时存储在浏览器和数据库中
if result['status_code'] == 2:
    session_id = secrets.token_urlsafe(16)
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    expire_time = (datetime.datetime.now() + datetime.timedelta(hours=+1)).strftime(GMT_FORMAT)
    # 将cookie存入浏览器中
    print('Set-Cookie: session_id={}; expires={}; path=/'.format(session_id, expire_time))
    # 将cookie存入数据库中
    insert_sql = 'insert Session(session_id, expire_time) values(\"{}\", \"{}\")'.format(
        session_id, expire_time)
    insert_or_update_data(insert_sql)

print()
print(json.dumps(result))
