# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-13 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Applies nullable change made to 0018_auto_20210714_2216.py after it was released
    """

    dependencies = [
        ('morango', '0018_auto_20210714_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfersession',
            name='transfer_stage',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[('initializing', 'Initializing'), ('serializing', 'Serializing'), ('queuing', 'Queuing'), ('transferring', 'Transferring'), ('dequeuing', 'Dequeuing'), ('deserializing', 'Deserializing'), ('cleanup', 'Cleanup')]),
        ),
        migrations.AlterField(
            model_name='transfersession',
            name='transfer_stage_status',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[('pending', 'Pending'), ('started', 'Started'), ('completed', 'Completed'), ('errored', 'Errored')]),
        ),
    ]
