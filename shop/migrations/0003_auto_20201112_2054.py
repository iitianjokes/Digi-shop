# Generated by Django 3.1.2 on 2020-11-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201112_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files'),
        ),
    ]
