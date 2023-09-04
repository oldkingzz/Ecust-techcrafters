# @Time: 2023-08-08 22:02
# @Author: DORK3333
# @File: urls.py
# Software: PyCharm
from django.urls import path
from . import views
app_name = "modumst"
urlpatterns = [
    path('', views.index, name='index'),
    # 其他URL模式
]
