# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20151225_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='customer',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
