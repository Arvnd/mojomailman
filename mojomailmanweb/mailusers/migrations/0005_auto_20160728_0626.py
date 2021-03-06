# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-28 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailusers', '0004_emailaddress_email_configured'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailaddress',
            name='num_emails_queued',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email_configured',
            field=models.BooleanField(default=False, max_length=255),
        ),
    ]
