# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20151225_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='registersms',
            name='customer',
        ),
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.ForeignKey(to='service.RegisterSMS'),
        ),
    ]
