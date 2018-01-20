# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrolnilist', '0024_remove_plankontrolaspecifikacija_plan_aktivnost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planaktivnost',
            name='planirano_opravilo',
        ),
        migrations.RemoveField(
            model_name='planaktivnost',
            name='projektno_mesto',
        ),
        migrations.RemoveField(
            model_name='plankontrolaskupina',
            name='plan_aktivnost',
        ),
        migrations.RemoveField(
            model_name='plankontrolaspecifikacija',
            name='plan_kontrola_skupina',
        ),
        migrations.RemoveField(
            model_name='plankontrolaspecifikacijaopcijaselect',
            name='plan_kontrola_specifikacija',
        ),
        migrations.AlterField(
            model_name='aktivnost',
            name='plan_aktivnost',
            field=models.ForeignKey(to='planiranje.PlanAktivnost', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kontrolaskupina',
            name='plan_kontrola_skupina',
            field=models.ForeignKey(verbose_name='planiranja skupina kontrol', to='planiranje.PlanKontrolaSkupina'),
        ),
        migrations.DeleteModel(
            name='PlanAktivnost',
        ),
        migrations.DeleteModel(
            name='PlanKontrolaSkupina',
        ),
        migrations.DeleteModel(
            name='PlanKontrolaSpecifikacija',
        ),
        migrations.DeleteModel(
            name='PlanKontrolaSpecifikacijaOpcijaSelect',
        ),
    ]
