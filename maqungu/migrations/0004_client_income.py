# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maqungu', '0003_auto_20170725_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Income',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]