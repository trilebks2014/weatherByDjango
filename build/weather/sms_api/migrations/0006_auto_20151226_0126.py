# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20151225_1453'),
        ('sms_api', '0005_remove_smsapipost_idsms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smsapipost',
            name='id',
        ),
        migrations.AddField(
            model_name='smsapipost',
            name='select',
            field=models.OneToOneField(primary_key=True, default=0, serialize=False, to='service.ServiceSMS'),
        ),
    ]
