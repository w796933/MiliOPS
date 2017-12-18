# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nginx', '0008_basicconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upstream_up_realserver_test', models.BooleanField(choices=[(True, '需要测试'), (False, '无需测试')], default=False, verbose_name='源站上线前是否需要测试连接源站')),
                ('upstream_up_realserver_testurl', models.CharField(blank=True, max_length=64, null=True, verbose_name='源站上线测试URL')),
            ],
        ),
    ]
