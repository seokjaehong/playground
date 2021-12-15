# Generated by Django 3.2.3 on 2021-12-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='종목명')),
                ('schedule', models.CharField(default='', max_length=20, verbose_name='공모주일정')),
                ('fixed_price', models.IntegerField(default=0, verbose_name='확정공모가')),
                ('hoped_price', models.CharField(default='', max_length=30, verbose_name='희망공모가')),
                ('compete_rate', models.TextField(default='', verbose_name='청약경쟁률')),
                ('underwriter', models.CharField(default='', max_length=100, verbose_name='주간사리스트')),
                ('ipo_id', models.IntegerField(default=0, verbose_name='IPO ID')),
                ('detail_link', models.URLField(blank=True, null=True, verbose_name='IPO Detail링크')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='시작일')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='종료일')),
                ('is_finished', models.BooleanField(default=False, verbose_name='청약종료여부')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
        ),
    ]
