# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 12:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('komment', '0010_auto_20160817_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_of_publish',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 12, 45, 23, 6237, tzinfo=utc)),
        ),
    ]
