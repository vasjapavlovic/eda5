# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerji', '0011_auto_20151025_1701'),
        ('etaznalastnina', '0002_auto_20151029_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastniskaEnotaInterna',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('oznaka', models.CharField(max_length=5, verbose_name='interna številka dela stavbe')),
                ('povrsina_tlorisna_neto', models.CharField(max_length=4, verbose_name='neto tlorisna površina')),
            ],
            options={
                'ordering': ('oznaka',),
                'verbose_name': 'etažna lastnina interna',
                'verbose_name_plural': 'etažna lastnina interna',
            },
        ),
        migrations.RenameModel(
            old_name='EtaznaLastninaElaborat',
            new_name='LastniskaEnotaElaborat',
        ),
        migrations.RemoveField(
            model_name='etaznalastninainterna',
            name='elaborat',
        ),
        migrations.RemoveField(
            model_name='etaznalastninainterna',
            name='lastnik',
        ),
        migrations.RemoveField(
            model_name='etaznalastninainterna',
            name='najemnik',
        ),
        migrations.RemoveField(
            model_name='etaznalastninainterna',
            name='placnik',
        ),
        migrations.DeleteModel(
            name='EtaznaLastninaInterna',
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='elaborat',
            field=models.ForeignKey(to='etaznalastnina.LastniskaEnotaElaborat'),
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='lastnik',
            field=models.ForeignKey(related_name='lastnik', to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='najemnik',
            field=models.ForeignKey(related_name='najemnik', null=True, blank=True, to='partnerji.Partner'),
        ),
        migrations.AddField(
            model_name='lastniskaenotainterna',
            name='placnik',
            field=models.ForeignKey(related_name='placnik', to='partnerji.Partner'),
        ),
    ]
