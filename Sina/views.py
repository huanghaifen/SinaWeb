# coding:utf-8
import datetime

from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from Sina.models import Items

def showSina(request):
    #从数据库取出新浪数据

    list =Items.objects.all() # [{'title': '标题1', 'url': 'http://test.com'}, {'title': '标题2', 'url': 'http://test.com'}]
    return render_to_response('sina.html', {'items': list})

def selectSina(request):
    # 按条件从数据库取出新浪数据
    list =Items.objects.filter(title__contains='%s' %request.GET['searchStr'])
    return render_to_response('sina.html', {'items': list})