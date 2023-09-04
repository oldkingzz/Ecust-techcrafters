# admin.py

from django.contrib import admin
from django.db import models
from django.forms import FileInput
from .models import course_model  # 确保正确导入 course_model
# Custom ModelAdmin class

class CourseModelAdmin(admin.ModelAdmin):
    # Set widget style for FileField
    formfield_overrides = {
        models.FileField: {'widget': FileInput(attrs={'accept': 'application/pdf'})},
    }

# Register your model and associate it with the custom ModelAdmin class
admin.site.register(course_model, CourseModelAdmin)