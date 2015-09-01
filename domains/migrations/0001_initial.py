# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('name', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('registrer_date', models.DateField()),
                ('release_date', models.DateField()),
                ('registrator', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('name', models.CharField(max_length=128, serialize=False, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='domain',
            name='zone',
            field=models.ForeignKey(to='domains.Zone'),
        ),
    ]
