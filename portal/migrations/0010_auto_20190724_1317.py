# Generated by Django 2.1.7 on 2019-07-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_application_school_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='passed',
            new_name='confirm',
        ),
    ]
