# Generated by Django 5.2 on 2025-05-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_alter_imagehash_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagehash',
            name='filename',
            field=models.TextField(default=None, null=True),
        ),
    ]
