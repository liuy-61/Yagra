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

# 查询该用户是否已经存在,存在则注册失败,不存在则注册
sql = 'select user_name from User where user_name = \"{}\"'.format(name)
if len(query_data(sql)) != 0:
    print("The user already exists, registration failed")
    print("<br>")
else:
    insert_sql = 'insert User(user_name, pwd) values(\"{}\", \"{}\")'.format(
        name, pwd)
    insert_or_update_data(insert_sql)
    print("Registered successfully")
    print("<br>")
