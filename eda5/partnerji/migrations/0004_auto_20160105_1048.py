# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partnerji', '0003_auto_20151219_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='user',
        ),
        migrations.AddField(
            model_name='oseba',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
