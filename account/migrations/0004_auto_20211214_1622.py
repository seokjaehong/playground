# Generated by Django 3.2.3 on 2021-12-14 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_account_info_list', to='account.account')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_member_info_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('account_info', 'member')},
            },
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
