# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='project',
        ),
        migrations.AddField(
            model_name='entry',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='time_tracking.Task'),
        ),
    ]