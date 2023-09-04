# @Time: 2023-07-29 17:11
# @Author: DORK3333
# @File: urls.py.py
# Software: PyCharm
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "navi"
urlpatterns = [
    path("", views.index, name="index"),
    path('<str:course_name>/', views.navi_view, name='navi'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
