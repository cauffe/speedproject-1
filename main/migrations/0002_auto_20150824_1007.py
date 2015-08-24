# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='info',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='up_votes',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='user',
        ),
    ]
