# Generated by Django 5.0.1 on 2024-01-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_blogpost_thumbnail_alter_blogpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
