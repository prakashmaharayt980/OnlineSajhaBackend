# Generated by Django 5.1.3 on 2024-12-06 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_postimage_news_newsdata_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdata',
            name='image',
        ),
        migrations.AddField(
            model_name='postimage',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_images', to='base.newsdata'),
        ),
    ]
