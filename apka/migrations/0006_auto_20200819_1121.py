# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0005_auto_20200818_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='key_words',
            field=models.TextField(default='key_words', verbose_name='S\u0142owa kluczowe'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='height',
            field=models.CharField(default='300', max_length=200, verbose_name='Wysoko\u015b\u0107 zdj\u0119cie'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='width',
            field=models.CharField(default='400', max_length=200, verbose_name='Szeroko\u015b\u0107 zdj\u0119cia'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Tw\xf3j e-mail'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Twoje imi\u0119'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='regulamin_1',
            field=models.BooleanField(default=False, verbose_name='Chc\u0119 zapisa\u0107 si\u0119 do newslettera, a co za tym idzie wyra\u017cam zgod\u0119 na otrzymanie na m\xf3j adres e-mail informacji o dzia\u0142alno\u015bci Zanurzeni w zieleni.'),
        ),
    ]
