# Generated by Django 5.1.3 on 2024-12-08 04:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_createadsimage_image_alter_postimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdata',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]