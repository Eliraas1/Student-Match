# Generated by Django 3.1.4 on 2021-01-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210107_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Admin_Rate_Student',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Rate_Teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='Admin_Rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Under_Average'), (2, '2 - Average'), (3, '3 - Great'), (4, '4 - Awesome'), (5, '4 - Master')], default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Admin_Rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - Under_Average'), (2, '2 - Average'), (3, '3 - Great'), (4, '4 - Awesome'), (5, '4 - Master')], default=0),
        ),
    ]
