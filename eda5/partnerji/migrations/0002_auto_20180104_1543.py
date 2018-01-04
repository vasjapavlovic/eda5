# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partnerji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oseba',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banka',
            name='partner',
            field=models.OneToOneField(blank=True, to='partnerji.Partner'),
        ),
    ]
