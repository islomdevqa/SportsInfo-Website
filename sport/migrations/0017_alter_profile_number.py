# Generated by Django 3.2.9 on 2021-11-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0016_auto_20211118_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
