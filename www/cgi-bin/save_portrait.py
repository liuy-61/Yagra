#!/home/ubuntu/anaconda3/envs/Yagra/bin/python3.8

import cgi
import os
import cgitb
import codecs
import sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
cgitb.enable()

# 获取文件名
form = cgi.FieldStorage()
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    images_dir = os.getcwd()
    images_dir = os.path.join(images_dir, "images")
    fn = os.path.basename(fileitem.filename)
    images_path = os.path.join(images_dir, fn)
    open(images_path, 'wb').write(fileitem.file.read())

    message = 'portrait uploaded successfully'

else:
    message = 'portrait upload failed'

print("Content-type:text/html")
print()
print(message)
