# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_audition_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audition',
            name='email',
            field=models.EmailField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audition',
            name='group',
            field=models.CharField(max_length=255, verbose_name=b'Group Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audition',
            name='location',
            field=models.TextField(default='', help_text=b'"City, State" or "City, Country"'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audition',
            name='voice_parts',
            field=models.ManyToManyField(to='board.VoicePart', null=True, verbose_name=b'Voice part(s)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='email',
            field=models.EmailField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='location',
            field=models.TextField(default='', help_text=b'"City, State" or "City, Country"'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='name',
            field=models.CharField(help_text=b'Your name (first only is ok!)', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='new_group_ok',
            field=models.BooleanField(default=False, help_text=b'Would you be ok with helping to start a new group?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlfg',
            name='voice_parts',
            field=models.ManyToManyField(help_text=b'Select any and all that apply!', to='board.VoicePart', null=True, verbose_name=b'Voice part(s)', blank=True),
            preserve_default=True,
        ),
    ]
