# Generated by Django 5.1.3 on 2024-12-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_rename_file_papersmodel_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='papersmodel',
            name='paper_data',
            field=models.TextField(null=True),
        ),
    ]
