# Generated by Django 3.1.2 on 2020-11-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('file', models.FileField(null=True, upload_to='uploads/files')),
                ('thumbnail', models.ImageField(upload_to='uploads/thumbnails')),
                ('links', models.CharField(max_length=100, null=True)),
                ('filesize', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/images')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
