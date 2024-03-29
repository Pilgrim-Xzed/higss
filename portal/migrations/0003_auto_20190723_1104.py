# Generated by Django 2.2.3 on 2019-07-23 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20190722_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='full_name_of_pupil',
        ),
        migrations.RemoveField(
            model_name='application',
            name='telephone_2',
        ),
        migrations.AddField(
            model_name='application',
            name='firstname_of_pupil',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='othername_of_pupil',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='surname_of_pupil',
            field=models.CharField(default=datetime.datetime(2019, 7, 23, 11, 4, 48, 405101, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
