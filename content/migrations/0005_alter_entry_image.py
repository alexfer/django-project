# Generated by Django 4.0 on 2022-11-21 05:11

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='', null=True, upload_to=content.models.Entry.entry_directory_path),
        ),
    ]