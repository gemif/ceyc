# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 14:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20170520_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoinscripcion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2017, 5, 20, 14, 57, 11, 198185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='examen',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2017, 5, 20, 14, 57, 11, 196358, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(default=datetime.datetime(2017, 5, 20, 14, 57, 11, 197582, tzinfo=utc)),
        ),
    ]
