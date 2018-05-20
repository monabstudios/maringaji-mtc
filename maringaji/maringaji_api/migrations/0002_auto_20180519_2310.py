# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 23:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maringaji_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applications',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applications',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL),
        ),
    ]
