# Generated by Django 5.1.3 on 2024-12-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news_images/')),
                ('type_of_news', models.CharField(max_length=100)),
                ('ads_box', models.ImageField(upload_to='ads_images/')),
                ('post_by', models.CharField(max_length=100)),
            ],
        ),
    ]