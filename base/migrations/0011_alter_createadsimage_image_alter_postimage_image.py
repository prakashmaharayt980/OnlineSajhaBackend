# Generated by Django 5.1.3 on 2024-12-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_createadsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createadsimage',
            name='image',
            field=models.ImageField(upload_to='CreateAdsSeperate/'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
