# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 21:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserManager',
        ),
    ]
