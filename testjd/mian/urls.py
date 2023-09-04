# @Time: 2023-08-09 21:48
# @Author: DORK3333
# @File: urls.py
# Software: PyCharm
from django.urls import path
from . import views
app_name = "mian"
urlpatterns = [
    path('', views.index, name='index'),
    # 其他URL模式
]