#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
# coding=utf-8

import pymysql

DBHOST = 'localhost'
DBUSER = 'root'
DBPWD = '5461'
DBNAME = 'yagra'
CHARSET = 'utf8'


def get_conn():
    """

    :return: mysql connection
    """
    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, passwd=DBPWD, database=DBNAME, charset=CHARSET)
        return db

    except pymysql.Error as e:
        print("Database connection failed：" + str(e))


def query_data(sql):
    """

    :param sql: SQL语句
    :return: list[dict]
    """
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


def insert_or_update_data(sql):
    """
    执行新增和更新
    :param sql: SQL语句
    :return:
    """
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()


def exist_db(db_name):
    """
    检查是否有名为db_name的数据库
    :param db_name:数据库库名
    :return:boolean
    """
    sql = 'SELECT count(SCHEMA_NAME) as SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME=\"{}\"'.format(
        db_name)
    res = query_data(sql)
    if res[0]['SCHEMA_NAME'] == 0:
        return False
    else:
        return True


def exist_tb_in_db(db_name, tb_name):
    """
    检查名为tb_name的数据库中，是否有名为db_name的表
    :param db_name: 数据库名
    :param tb_name: 表名
    :return: boolean
    """
    sql = 'select count(*) from information_schema.TABLES t where t.TABLE_SCHEMA = \"{}\" ' \
          'and t.TABLE_NAME = \"{}\";'.format(db_name, tb_name)

    res = query_data(sql)
    if res[0]['count(*)'] == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    sql = 'select * from User'
    res = query_data(sql)
    debug = 0