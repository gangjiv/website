# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-13 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0119_auto_20181213_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internselection',
            name='initial_feedback_due',
            field=models.DateField(blank=True, verbose_name='Date initial feedback form opens'),
        ),
        migrations.AlterField(
            model_name='internselection',
            name='initial_feedback_opens',
            field=models.DateField(blank=True, verbose_name='Date initial feedback form opens'),
        ),
    ]
