# Generated by Django 3.1.7 on 2021-03-23 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20210323_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date',
        ),
    ]
