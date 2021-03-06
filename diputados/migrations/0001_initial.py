# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-10 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diputado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('foto', models.ImageField(null=True, upload_to='/assets/images')),
                ('suplente', models.CharField(max_length=100)),
            ],
        ),
    ]
