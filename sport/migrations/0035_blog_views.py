# Generated by Django 3.2.9 on 2021-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0034_news_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]