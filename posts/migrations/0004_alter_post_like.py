# Generated by Django 4.2.1 on 2023-05-14 23:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_remove_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL, verbose_name='좋아요'),
        ),
    ]
