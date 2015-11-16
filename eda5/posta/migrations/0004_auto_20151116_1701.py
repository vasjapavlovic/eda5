# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0002_skupinapartnerjev_oznaka'),
        ('posta', '0003_auto_20151116_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arhiviranje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('elektronski', models.BooleanField(default=True, verbose_name='elektronski hramba')),
                ('fizicni', models.BooleanField(default=False, verbose_name='fizični hramba')),
                ('arhiviral', models.ForeignKey(to='partnerji.Oseba')),
                ('dokument', models.OneToOneField(to='posta.Dokument')),
            ],
            options={
                'verbose_name_plural': 'arhiviranje',
                'verbose_name': 'arhiviranje',
            },
        ),
        migrations.CreateModel(
            name='ArhivLokacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('oznaka', models.CharField(verbose_name='oznaka', max_length=10)),
                ('naziv', models.CharField(verbose_name='naziv', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'lokacije arhiviranja',
                'verbose_name': 'lokacija arhiviranja',
            },
        ),
        migrations.AlterModelOptions(
            name='arhiv',
            options={'verbose_name_plural': 'arhivi', 'verbose_name': 'arhiv'},
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='arhiviral',
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='created',
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='dokument',
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='elektronski',
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='fizicni',
        ),
        migrations.RemoveField(
            model_name='arhiv',
            name='updated',
        ),
        migrations.AddField(
            model_name='arhiv',
            name='naziv',
            field=models.CharField(default='abc', verbose_name='naziv', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arhiv',
            name='oznaka',
            field=models.CharField(default='abc', verbose_name='oznaka', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arhivlokacija',
            name='arhiv',
            field=models.ForeignKey(to='posta.Arhiv'),
        ),
        migrations.AddField(
            model_name='arhiviranje',
            name='lokacija_hrambe',
            field=models.ForeignKey(verbose_name='lokacija hrambe', null=True, to='posta.ArhivLokacija', blank=True),
        ),
    ]
