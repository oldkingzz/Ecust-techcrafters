from django.db import models

# Create your models here.
from django.db import models

class Person_a(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    introduction = models.TextField(verbose_name='介绍')
    picture = models.ImageField(upload_to='static/images_people/', verbose_name='图片', blank=True, null=True)
    def __str__(self):
        return self.name
class Person_b(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    introduction = models.TextField(verbose_name='介绍')
    picture = models.ImageField(upload_to='static/images_people/', verbose_name='图片', blank=True, null=True)

    def __str__(self):
        return self.name
