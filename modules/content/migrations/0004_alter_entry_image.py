# Generated by Django 4.0 on 2022-11-20 14:13

from django.db import migrations, models
import modules


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0003_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(null=True, upload_to=modules.content.models.Entry.entry_directory_path),
        ),
    ]