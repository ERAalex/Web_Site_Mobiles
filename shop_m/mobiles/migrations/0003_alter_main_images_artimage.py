# Generated by Django 4.0.3 on 2022-07-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_main_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_images',
            name='artimage',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/home', verbose_name='изображение'),
        ),
    ]
