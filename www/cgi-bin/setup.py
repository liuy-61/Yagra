from mysql import query_data, insert_or_update_data, exist_db, exist_tb_in_db, DBNAME

# 不存在数据库则先创建
sql = 'CREATE DATABASE if not exists {} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'.format(DBNAME)
query_data(sql)

# 首先判断数据表是否存在，不存在则先创建对应的表
if not exist_tb_in_db(db_name=DBNAME, tb_name="User"):
    sql = 'use {};'.format(DBNAME)
    query_data(sql)
    sql = "create table User(user_name char(30) primary key, pwd char(30));"
    query_data(sql)

if not exist_tb_in_db(db_name=DBNAME, tb_name="Session"):
    sql = 'use {};'.format(DBNAME)
    query_data(sql)
    sql = "create table Session(session_id char(32) primary key, expire_time char(32));"
    query_data(sql)
