# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0003_auto_20151226_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='smsApiPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idsms', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('REQID', models.CharField(max_length=200)),
                ('LABELID', models.CharField(max_length=200)),
                ('CONTRACTTYPEID', models.CharField(max_length=200)),
                ('CONTRACTID', models.CharField(max_length=200)),
                ('TEMPLATEID', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
