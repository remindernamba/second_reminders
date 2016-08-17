# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 12:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_auto_20160817_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='date_of_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 17, 12, 45, 26, 891580, tzinfo=utc), null=True, verbose_name='\u0414\u0430\u0442\u0430 \u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='date_of_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 17, 12, 45, 26, 891632, tzinfo=utc), null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u043e'),
        ),
    ]
