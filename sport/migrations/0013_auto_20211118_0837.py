# Generated by Django 3.2.9 on 2021-11-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0012_auto_20211118_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='euronews',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
