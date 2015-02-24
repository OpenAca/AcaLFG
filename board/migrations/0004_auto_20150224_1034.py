# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150224_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='audition',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userlfg',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
