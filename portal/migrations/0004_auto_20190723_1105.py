# Generated by Django 2.2.3 on 2019-07-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20190723_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='firstname_of_pupil',
            field=models.CharField(max_length=255),
        ),
    ]
