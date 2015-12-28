# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20151225_0324'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='selectService',
            field=models.ForeignKey(default=0, to='service.RegisterSMS'),
        ),
    ]
