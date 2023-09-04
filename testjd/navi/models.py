from django.db import models

from django.db import models
 # 确保正确导入 course_model
def validate_html_extension(value):
    if not value.name.endswith('.html'):
        raise ValidationError("文件必须为HTML格式")
class course_model(models.Model):
    name = models.CharField(max_length=100, default='名字请以chap_ + 数字组成')
    course_name = models.TextField()
    ppt = models.FileField(upload_to='static/pdfs/')  # 存储PDF文件路径的字段
    long_text = models.TextField()  # 存储很长的文本内容的字段
    notes = models.FileField(upload_to='static/notes/', validators=[validate_html_extension])

    # Add other fields as per your model's structure

    def __str__(self):
        return self.name
