#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8

import cgi
import cgitb
import pymysql
from mysql import query_data, insert_or_update_data, exist_db, exist_tb_in_db, DBNAME

# 获取用户名和密码
form = cgi.FieldStorage()
name = form.getvalue("name")
pwd = form.getvalue("pwd")

print("Content-type:text/html")
print()
print("name: " + name)
print("pwd: " + pwd)
print("<br>")


# 在接收到用户名和密码之后，首先判断用户表是否存在，不存在则先创建对应的表
if not exist_tb_in_db(db_name=DBNAME, tb_name="User"):
    sql = 'use {};'.format(DBNAME)
    query_data(sql)
    sql = "create table User(user_name char(30) primary key, pwd char(30));"
    query_data(sql)

#  根据用户提供的用户名, 查找有无对应的用户,如果没有则提醒用户进行注册,如果密码错误的话提示登录失败
sql = 'select user_name,pwd from User where user_name = \"{}\"'.format(name)
res = query_data(sql)
if len(res) == 0:
    print("The user is not registered, Please register firstly")
elif res[0]['pwd'] == pwd:
    print("login successfully")
else:
    print("login failure")


