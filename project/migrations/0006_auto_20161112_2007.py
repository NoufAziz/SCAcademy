# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_lecture_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cource',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='lecture',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
