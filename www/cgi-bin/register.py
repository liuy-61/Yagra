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


# 查询该用户是否已经存在,存在则注册失败,不存在则注册
sql = 'select user_name from User where user_name = \"{}\"'.format(name_front)
if len(query_data(sql)) != 0:
    result = {
        "status_code": 0,
        "status_str": "register failed, the user user has been registered, please register again."}
else:
    insert_sql = 'insert User(user_name, pwd) values(\"{}\", \"{}\")'.format(
        name_front, pwd_front)
    insert_or_update_data(insert_sql)
    result = {
        "status_code": 1,
        "status_str": "register successfully."}

print("Content-type:text/html")
print()
print(json.dumps(result))