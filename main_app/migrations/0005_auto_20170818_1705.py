# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20170818_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(upload_to=b'image/'),
        ),
    ]
