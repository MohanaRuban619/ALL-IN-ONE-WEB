# Generated by Django 4.0 on 2022-01-17 06:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Web_sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Of_Site', models.CharField(max_length=200)),
                ('Image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
                ('Site_Link', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=10000)),
            ],
        ),
    ]