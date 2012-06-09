#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Written by johncan 2012-06-09
import os
import sys
import time
#add vpanth's path to sys.path,then define vpanauth.settings
sys.path.append('/data/django/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'vpnauth.settings'
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#import our Log models,then we can store our log in DB
from vpnauth.vpn.models import VpnLog


#The main func
def main():
    #Get the username and passwod from os.environment
    username = os.environ['username']
    password = os.environ['password']
    

    t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    #Start to authenticate
    try:
        #Try to get the user,if the user is exist,then go to next
        User.objects.get(username=username)
        #Check the user's password
        user = authenticate(username=username, password=password)
        if user is not None:
            authlog=VpnLog(username=username,content="Successful authentication",login_time=t,result=1)
            authlog.save() 
            sys.exit(0)     
        #Password error.    
        else:
            authlog=VpnLog(username=username,content="Password error.",login_time=t,result=0)
            authlog.save() 
            sys.exit(1)                   
    #If the user is not exist    
    except User.DoesNotExist:
        authlog=VpnLog(username=username,content="User doesn't exist.",login_time=t,result=0)
        authlog.save() 
        sys.exit(1)           

if __name__ == "__main__": 
    main()
