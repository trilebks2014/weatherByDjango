# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_selectservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='selectService',
            field=models.ForeignKey(default=0, to='service.ServiceSMS'),
        ),
    ]
