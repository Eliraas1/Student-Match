# Generated by Django 3.0.7 on 2021-01-07 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210108_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='student',
            new_name='reported_on',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='teacher',
            new_name='teacher_reported',
        ),
    ]
