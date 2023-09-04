from django.contrib import admin
from django.db import models
from django.forms import FileInput
from .models import Person_a, Person_b  # 确保正确导入 Person 模型

# Custom ModelAdmin class
class PersonAdmin(admin.ModelAdmin):
    # 设置 FileField 的小部件样式
    formfield_overrides = {
        models.ImageField: {'widget': FileInput(attrs={'accept': 'image/png'})},
    }

# 注册您的模型并将其与自定义 ModelAdmin 类关联
admin.site.register(Person_a, PersonAdmin)
admin.site.register(Person_b, PersonAdmin)
