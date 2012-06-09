from django.db import models

class VpnLog(models.Model):
    username=models.CharField(max_length=50)
    content=models.CharField(max_length=512)
    login_time=models.DateTimeField(auto_now=False)
    result=models.BooleanField(0)

