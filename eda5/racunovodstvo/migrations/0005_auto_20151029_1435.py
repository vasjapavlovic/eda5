# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('racunovodstvo', '0004_auto_20151029_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='PodKonto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('oznaka', models.CharField(max_length=10)),
                ('naziv', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'pod konti',
                'verbose_name': 'pod konto',
            },
        ),
        migrations.AddField(
            model_name='konto',
            name='naziv',
            field=models.CharField(default='Upravljanje', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='konto',
            name='oznaka',
            field=models.CharField(default='100', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skupinavrstestroska',
            name='naziv',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skupinavrstestroska',
            name='oznaka',
            field=models.CharField(default='U-ONU-01', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skupinavrstestroska',
            name='zap_st',
            field=models.IntegerField(default=0, verbose_name='zaporedna Številka'),
        ),
        migrations.AddField(
            model_name='strosek',
            name='datum_storitve_do',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='datum_storitve_od',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='delilnik_kljuc',
            field=models.CharField(choices=[('lastniski_delez', 'lastniški delež'), ('povrsina', 'površina enote'), ('st_enot', 'število enot'), ('oseba', 'število oseb')], default='x', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='delilnik_vrsta',
            field=models.CharField(choices=[('fiksni', 'fiksni strošek'), ('vuporabi', 'LE v uporabi'), ('delilniki', 'po priloženem delilniku')], default='c', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='is_strosek_posameznidel',
            field=models.BooleanField(default=False, verbose_name='strosek na posameznem delu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='naziv',
            field=models.CharField(default='v', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='oznaka',
            field=models.CharField(default='v', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='stopnja_ddv',
            field=models.DecimalField(default=0.22, decimal_places=3, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='vrednost',
            field=models.DecimalField(default=100, decimal_places=2, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strosek',
            name='vrsta_stroska',
            field=models.ForeignKey(default=1, to='racunovodstvo.VrstaStroska'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrstastroska',
            name='naziv',
            field=models.CharField(default='v', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrstastroska',
            name='oznaka',
            field=models.CharField(default='v', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrstastroska',
            name='skupina',
            field=models.ForeignKey(default=1, to='racunovodstvo.SkupinaVrsteStroska'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrstastroska',
            name='zap_st',
            field=models.IntegerField(default=0, verbose_name='zaporedna Številka'),
        ),
        migrations.AddField(
            model_name='podkonto',
            name='skupina',
            field=models.ForeignKey(to='racunovodstvo.Konto'),
        ),
        migrations.AddField(
            model_name='skupinavrstestroska',
            name='skupina',
            field=models.ForeignKey(default=1, to='racunovodstvo.PodKonto'),
            preserve_default=False,
        ),
    ]
