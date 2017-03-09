# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_usermanager'),
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='all_likes',
        ),
        migrations.AddField(
            model_name='secret',
            name='all_likes',
            field=models.ManyToManyField(related_name='all_users', to='login.User'),
        ),
    ]
