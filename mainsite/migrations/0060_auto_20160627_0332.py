# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 22:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0059_auto_20160627_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 6, 26, 22, 2, 36, 244236, tzinfo=utc)),
        ),
    ]