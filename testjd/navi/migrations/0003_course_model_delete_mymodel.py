# Generated by Django 4.2.3 on 2023-07-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi', '0002_mymodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名字请以chap_ + 数字组成', max_length=100)),
                ('course_name', models.TextField()),
                ('ppt', models.FileField(upload_to='static/pdfs/')),
                ('long_text', models.TextField()),
                ('notes', models.FileField(upload_to='static/notes/')),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
