# Generated by Django 2.1.7 on 2019-07-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20190723_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='passports/'),
        ),
    ]
