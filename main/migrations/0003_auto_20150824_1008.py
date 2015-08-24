# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150824_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedmodel',
            name='down_votes',
            field=models.ManyToManyField(related_name='down_votes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='image',
            field=models.ImageField(null=True, upload_to=b'image', blank=True),
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='up_votes',
            field=models.ManyToManyField(related_name='up_votes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='speedmodel',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
