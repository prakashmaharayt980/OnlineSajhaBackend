# Generated by Django 5.1.3 on 2024-12-03 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_newsdata_ads_image_remove_newsdata_postimages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adsimage',
            name='images',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='images',
        ),
        migrations.AddField(
            model_name='adsimage',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads_images', to='base.newsdata'),
        ),
        migrations.AddField(
            model_name='postimage',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_images', to='base.newsdata'),
        ),
    ]
