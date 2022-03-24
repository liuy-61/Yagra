#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8
# coding=utf-8
import cgi
import cgitb
import json
import sys

cgitb.enable()
form = cgi.FieldStorage()
ID = form.getvalue("ID")
NAME = form.getvalue("NAME")
result = {"ID":ID, "NAME":NAME}
# todo something

print("Content-type:application/json")
print(json.dumps(result))



