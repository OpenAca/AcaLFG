# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150209_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='audition',
            name='is_verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='audition',
            name='verification_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlfg',
            name='is_verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userlfg',
            name='verification_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
