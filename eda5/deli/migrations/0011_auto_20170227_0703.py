# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deli', '0010_auto_20170227_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lokacija',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('etaza', models.ForeignKey(to='deli.Etaza', verbose_name='Etaža')),
                ('prostor', models.OneToOneField(to='deli.DelStavbe', verbose_name='Prostor')),
            ],
            options={
                'verbose_name_plural': 'Relacije Prostor/Etaža',
                'ordering': ['prostor__oznaka'],
                'verbose_name': 'Relacija Prostor/Etaža',
            },
        ),
        migrations.RemoveField(
            model_name='relacijaprostoretaza',
            name='etaza',
        ),
        migrations.RemoveField(
            model_name='relacijaprostoretaza',
            name='prostor',
        ),
        migrations.AlterField(
            model_name='projektnomesto',
            name='lokacija',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Lokacija v Stavbi', to='deli.Lokacija'),
        ),
        migrations.DeleteModel(
            name='RelacijaProstorEtaza',
        ),
    ]
