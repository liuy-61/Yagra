#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
import secrets
import cgi
import datetime
import os
import json
import cgitb
from http import cookies
from mysql import query_data, insert_or_update_data, exist_db, exist_tb_in_db, DBNAME
from cookie import get_cookie

cgitb.enable()
# 从浏览器中取出cookie
cookie_front = get_cookie("session_id")
if cookie_front is None:
    result = {
        "status_code": 0,
        "status_str": "You have not logged in yet, please login first"}
else:
    # 从数据库查找看是否存在对应的cookie
    sql = 'select session_id from Session where session_id = \"{}\"'.format(
        cookie_front)
    res = query_data(sql)
    if len(res) == 0:
        result = {
            "status_code": 0,
            "status_str": "You have not logged in yet, please login first"}
    else:
        result = {
            "status_code": 1,
            "status_str": "You have logged"}

print("Content-type:text/html")
print()
print(json.dumps(result))
