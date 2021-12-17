# Generated by Django 3.2.3 on 2021-12-17 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0004_delete_ipostockbroker'),
        ('account', '0003_delete_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='청약 추천내용')),
                ('is_possible', models.BooleanField(default=False, verbose_name='청약가능여부')),
                ('order_cnt', models.IntegerField(default=0, verbose_name='청약신청수량')),
                ('order_datetime', models.DateTimeField(blank=True, null=True, verbose_name='청약신청 날짜')),
                ('is_order', models.BooleanField(default=False, verbose_name='청약완료여부')),
                ('description', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('ipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.ipo')),
                ('order_stock_broker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.stockbroker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
