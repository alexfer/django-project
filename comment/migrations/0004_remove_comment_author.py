# Generated by Django 4.0 on 2022-11-19 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]