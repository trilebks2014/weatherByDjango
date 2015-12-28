# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0004_auto_20151226_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smsapipost',
            name='idsms',
        ),
    ]
