# Generated by Django 5.1.3 on 2024-12-06 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='papersmodel',
            old_name='file',
            new_name='files',
        ),
    ]
