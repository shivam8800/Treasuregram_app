# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasure',
            name='img_url',
        ),
        migrations.AddField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default=1, upload_to=b'treasure_image'),
            preserve_default=False,
        ),
    ]
