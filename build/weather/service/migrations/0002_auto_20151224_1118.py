# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registersms',
            name='id',
        ),
        migrations.AlterField(
            model_name='registersms',
            name='select',
            field=models.OneToOneField(primary_key=True, serialize=False, to='service.ServiceSMS'),
        ),
    ]
