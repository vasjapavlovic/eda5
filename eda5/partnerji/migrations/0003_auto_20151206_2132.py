# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_auto_20151203_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skupinapartnerjev',
            old_name='oznaka',
            new_name='davcna_st',
        ),
    ]
