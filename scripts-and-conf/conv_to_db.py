#!/usr/bin/python2.7
#coding=utf-8
#put this scripts in /data/django/vpnauth
import os
import re
from django.contrib.auth.models import User

#原有密码文件
pwfile='/etc/openvpn/psw-file'
#匹配用户名和密码的正则
up = '([a-z]*) (.*)'
p = re.compile(up)

f = open(pwfile,"r")

for a in p.findall(f.read()):
    u=User.objects.create_user(username=a[0],password=a[1],email=a[0]+'@example.com')
    u.save
	
	
f.close()
