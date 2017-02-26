# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_g', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Description content of blog post', max_length=10000)),
                ('post_date', models.DateField(blank=True, null=True)),
                ('author', models.ManyToManyField(help_text='Select Author for this Blog Post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
    ]
