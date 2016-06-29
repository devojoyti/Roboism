# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 16:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20160620_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2016, 6, 20, 16, 8, 12, 618087, tzinfo=utc)),
        ),
    ]