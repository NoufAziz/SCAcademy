# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20161116_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_c',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.Course'),
        ),
    ]
