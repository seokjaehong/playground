# Generated by Django 3.2.3 on 2021-12-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_accounts'),
        ('stocks', '0002_ipostockbroker'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo',
            name='stock_brokers',
            field=models.ManyToManyField(to='account.StockBroker'),
        ),
    ]
