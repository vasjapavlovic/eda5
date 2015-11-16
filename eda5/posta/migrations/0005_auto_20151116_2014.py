# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posta', '0004_auto_20151116_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArhivMesto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=10)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
                ('arhiv', models.ForeignKey(to='posta.Arhiv')),
            ],
            options={
                'verbose_name_plural': 'arhivska mesta',
                'verbose_name': 'arhivsko mesto',
            },
        ),
        migrations.RemoveField(
            model_name='arhivlokacija',
            name='arhiv',
        ),
        migrations.RemoveField(
            model_name='arhiviranje',
            name='dokument',
        ),
        migrations.AddField(
            model_name='dokument',
            name='arhiviranje',
            field=models.OneToOneField(to='posta.Arhiviranje', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(to='posta.ArhivMesto', blank=True, null=True, verbose_name='lokacija hrambe'),
        ),
        migrations.DeleteModel(
            name='ArhivLokacija',
        ),
    ]
