# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-15 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0003_auto_20200815_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='foto',
            field=models.CharField(default='link do zdj\u0119cia', max_length=700, verbose_name='Zdj\u0119cie'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='height',
            field=models.CharField(default='200', max_length=200, verbose_name='Wysoko\u015b\u0107 zdj\u0119cie'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='width',
            field=models.CharField(default='400', max_length=200, verbose_name='Szeroko\u015b\u0107 zdj\u0119cia'),
        ),
    ]