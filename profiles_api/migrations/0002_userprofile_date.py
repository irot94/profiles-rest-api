# Generated by Django 3.1.7 on 2021-03-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date',
            field=models.DateField(default='1980-01-01', unique=True),
        ),
    ]
