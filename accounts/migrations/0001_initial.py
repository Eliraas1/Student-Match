# Generated by Django 3.0.3 on 2021-01-06 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='summaries')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Role', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], default=1, max_length=300, null=True)),
                ('Profile_pic', models.ImageField(default='default.gif', upload_to='profile_pic')),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Famale')], max_length=300, null=True)),
                ('location', models.CharField(max_length=20)),
                ('study_choice', models.CharField(choices=[('aerospace engineering', 'Aerospace Engineering'), ('architecture', 'Architecture'), ('business', 'Business'), ('chemical engineering', 'Chemical Engineering'), ('civil engineering', 'Civil Engineering'), ('computer engineering', 'Computer Engineering'), ('computer science', 'Computer Science'), ('economics', 'Economics'), ('education', 'Education'), ('electrical engineering', 'Electrical Engineering'), ('engineering', 'Engineering'), ('graphic design', 'Graphic Design'), ('industrial engineering', 'Industrial Engineering'), ('software engineering', 'Software Engineering')], max_length=300, null=True)),
                ('years_in_academy', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_student', models.BooleanField(default=False)),
                ('Role', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], default=0, max_length=300, null=True)),
                ('Profile_pic', models.ImageField(default='default2.jpg', upload_to='profile_pic')),
                ('description', models.TextField(blank=True, null=True)),
                ('cv', models.FileField(upload_to='cv')),
                ('undergraduate', models.CharField(choices=[('BA', 'Bachelor'), ('BSc', 'Bachelor of Science'), ('MA', 'Master'), ('MSc', 'Master of Science'), ('PhD', 'Doctor of Philosophy')], max_length=300, null=True)),
            ],
        ),
    ]
