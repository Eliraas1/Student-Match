# Generated by Django 3.0.7 on 2021-01-07 00:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_student_admin_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Report',
        ),
    ]
