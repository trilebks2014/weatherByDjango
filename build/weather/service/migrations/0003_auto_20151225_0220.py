# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20151224_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registersms',
            name='customer',
            field=models.ManyToManyField(related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicesms',
            name='services',
            field=models.CharField(default=b'Day By Day', unique=True, max_length=200),
        ),
    ]
