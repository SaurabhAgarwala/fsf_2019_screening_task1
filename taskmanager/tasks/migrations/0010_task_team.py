# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-28 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190326_1253'),
        ('tasks', '0009_auto_20190328_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team'),
        ),
    ]
