#coding:utf-8
from __future__ import unicode_literals

from time import timezone

from django.db import models

# Create your models here.

class Items(models.Model):
      title = models.CharField(u'标题', max_length=256)
      url=models.CharField(u'链接',max_length=500)
      content = models.TextField(u'内容')
      pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
      updatetime = models.DateTimeField(u'更新时间', auto_now=True, null=True)
