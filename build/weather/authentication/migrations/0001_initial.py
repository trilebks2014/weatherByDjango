# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('public_email', models.EmailField(null=True, blank=True, max_length=254)),
                ('location', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('mendeley_token', models.CharField(null=True, blank=True, max_length=2000)),
                ('dropbox_token', models.CharField(null=True, blank=True, max_length=2000)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
