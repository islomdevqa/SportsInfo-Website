# Generated by Django 3.2.9 on 2021-11-18 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0021_alter_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
