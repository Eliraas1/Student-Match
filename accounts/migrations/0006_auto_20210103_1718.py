# Generated by Django 3.0.3 on 2021-01-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210103_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
