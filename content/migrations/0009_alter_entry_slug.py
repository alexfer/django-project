# Generated by Django 4.0 on 2022-11-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_entry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(max_length=512, null=True),
        ),
    ]
