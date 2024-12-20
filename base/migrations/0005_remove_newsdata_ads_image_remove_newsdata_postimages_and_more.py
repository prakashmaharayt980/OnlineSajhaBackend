# Generated by Django 5.1.3 on 2024-12-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_newsdata_ads_image_alter_newsdata_postimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdata',
            name='ads_Image',
        ),
        migrations.RemoveField(
            model_name='newsdata',
            name='postImages',
        ),
        migrations.CreateModel(
            name='AdsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads_images/')),
                ('images', models.ManyToManyField(blank=True, related_name='ads_images', to='base.newsdata')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('images', models.ManyToManyField(blank=True, related_name='post_images', to='base.newsdata')),
            ],
        ),
    ]
