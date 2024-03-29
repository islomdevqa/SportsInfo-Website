# Generated by Django 3.2.9 on 2021-11-12 17:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0008_blog_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
