# @Time: 2023-09-02 19:21
# @Author: DORK3333
# @File: urls.py
# Software: PyCharm
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "legend"
urlpatterns = [
    path("", views.index, name="index"),
    path('legend_sol/<str:person_name>/', views.legend_detail_A, name='legend_detail'),
    path('legend_mec/<str:person_name>/', views.legend_detail_B, name='legend_detail_mec'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
