#coding=utf-8

from django import forms
from django.contrib.auth.models import User

class VpnForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30,required=True)
    password = forms.CharField(label='原密码',max_length=30, widget=forms.PasswordInput(), required=True) 
#    newpass = forms.CharField(label='新密码',max_length=30, widget=forms.PasswordInput(), required=True) 
#    connewpass = forms.CharField(label='确认密码',max_length=30, widget=forms.PasswordInput(), required=True) 

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("没有该用户")
        return username

"""    def clean_connewpass(self):
        newpass = self.cleaned_data.get("newpass","")
        connewpass = self.cleaned_data["connewpass"]
        if newpass != connewpass:
            raise forms.ValidationError("新密码不匹配")
        return connewpass
"""
