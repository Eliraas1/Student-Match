# Generated by Django 3.0.7 on 2021-01-07 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210108_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='reported_on',
            new_name='user',
        ),
    ]
