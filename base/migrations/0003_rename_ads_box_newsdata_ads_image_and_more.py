# Generated by Django 5.1.3 on 2024-12-02 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_newsdata_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsdata',
            old_name='ads_box',
            new_name='ads_Image',
        ),
        migrations.RenameField(
            model_name='newsdata',
            old_name='image',
            new_name='postImages',
        ),
    ]
