# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='albums.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artists.Artist'),
            preserve_default=False,
        ),
    ]
    