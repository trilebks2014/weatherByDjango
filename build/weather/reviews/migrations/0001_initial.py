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
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(null=True, blank=True, max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('objective', models.TextField(max_length=1000)),
                ('status', models.CharField(default='U', choices=[('U', 'Unpublished'), ('P', 'Published')], max_length=1)),
                ('quality_assessment_cutoff_score', models.FloatField(default=0.0)),
                ('population', models.CharField(blank=True, max_length=200)),
                ('intervention', models.CharField(blank=True, max_length=200)),
                ('comparison', models.CharField(blank=True, max_length=200)),
                ('outcome', models.CharField(blank=True, max_length=200)),
                ('context', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('co_authors', models.ManyToManyField(related_name='co_authors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('is_default', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='review',
            name='sources',
            field=models.ManyToManyField(to='reviews.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('name', 'author')]),
        ),
    ]
