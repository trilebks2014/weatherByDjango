# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20151225_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dropbox_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mendeley_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='public_email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='url',
        ),
    ]
