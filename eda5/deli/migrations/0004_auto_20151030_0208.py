# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etaznalastnina', '0007_lastniskaskupina_lastniska_enota'),
        ('deli', '0003_auto_20151030_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelStavbe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=255)),
                ('shema', models.FileField(blank=True, upload_to='shema_directory_path', verbose_name='shema sistema')),
                ('lastniska_skupina', models.ForeignKey(blank=True, verbose_name='lastniška skupina', to='etaznalastnina.LastniskaSkupina', null=True)),
                ('podskupina', models.ForeignKey(to='deli.Podskupina')),
            ],
            options={
                'verbose_name_plural': 'deli stavbe',
                'verbose_name': 'del stavbe',
                'ordering': ['oznaka'],
            },
        ),
        migrations.RemoveField(
            model_name='del',
            name='lastniska_skupina',
        ),
        migrations.RemoveField(
            model_name='del',
            name='skupina',
        ),
        migrations.RemoveField(
            model_name='element',
            name='skupina',
        ),
        migrations.DeleteModel(
            name='Del',
        ),
        migrations.AddField(
            model_name='element',
            name='del_stavbe',
            field=models.ForeignKey(to='deli.DelStavbe', default=5),
            preserve_default=False,
        ),
    ]
