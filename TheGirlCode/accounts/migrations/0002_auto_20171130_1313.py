# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='progress',
            field=models.IntegerField(default=1),
        ),
    ]
