# Generated by Django 3.2.3 on 2021-12-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(choices=[('한식', '한식'), ('중식', '중식'), ('양식', '양식'), ('일식', '일식'), ('기타', '기타')], max_length=20),
        ),
    ]
