# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0003_auto_20151206_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strosek',
            name='vrednost',
        ),
        migrations.AddField(
            model_name='racun',
            name='osnova_0',
            field=models.DecimalField(null=True, verbose_name='osnova brez ddv', max_digits=7, blank=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='racun',
            name='osnova_1',
            field=models.DecimalField(null=True, verbose_name='osnova nižja stopnja', max_digits=7, blank=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='racun',
            name='osnova_2',
            field=models.DecimalField(null=True, verbose_name='osnova višja stopnja', max_digits=7, blank=True, decimal_places=2),
        ),
        migrations.AddField(
            model_name='strosek',
            name='osnova',
            field=models.DecimalField(verbose_name='osnova za ddv', max_digits=7, default=1, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='strosek',
            name='stopnja_ddv',
            field=models.IntegerField(verbose_name='stopnja DDV', choices=[(0, 'neobdavčeno'), (1, 'nižja stopnja'), (2, 'višja stopnja')]),
        ),
    ]
