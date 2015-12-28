# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smsapipost',
            name='language',
        ),
        migrations.RemoveField(
            model_name='smsapipost',
            name='style',
        ),
    ]
