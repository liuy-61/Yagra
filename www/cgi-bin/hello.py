#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
# coding=utf-8
import datetime
import secrets
print("Content-type:text/html")
session_id = secrets.token_urlsafe(16)
# TODO 这里之后需要删除
session_id = "54615461"
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
expire_time = (datetime.datetime.now() + datetime.timedelta(hours=+1)).strftime(GMT_FORMAT)
print('Set-Cookie: session_id={}; expires={}'.format(session_id, expire_time))
print()