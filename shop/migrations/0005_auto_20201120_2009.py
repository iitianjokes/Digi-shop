# Generated by Django 3.1.2 on 2020-11-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobileno',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
