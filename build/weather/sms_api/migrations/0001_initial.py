# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='smsApiPost',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('REQID', models.CharField(max_length=200)),
                ('LABELID', models.CharField(default=b'12911', max_length=200)),
                ('CONTRACTTYPEID', models.CharField(default=b'1', max_length=200)),
                ('CONTRACTID', models.CharField(default=b'19741', max_length=200)),
                ('TEMPLATEID', models.CharField(default=b'78382', max_length=200)),
                ('ISTELCOSUB', models.CharField(default=b'0', max_length=2)),
                ('AGENTID', models.CharField(default=b'191', max_length=200)),
                ('APIUSER', models.CharField(default=b'kdvnptqnm', max_length=200)),
                ('APIPASS', models.CharField(default=b'kdvnptqnm', max_length=200)),
                ('USERNAME', models.CharField(default=b'kdvnptqnm', max_length=200)),
                ('select', models.OneToOneField(primary_key=True, default=0, serialize=False, to='service.ServiceSMS')),
            ],
        ),
    ]
