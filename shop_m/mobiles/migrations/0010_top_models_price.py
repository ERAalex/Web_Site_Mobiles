# Generated by Django 4.0.3 on 2022-07-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0009_remove_top_models_show_art_top_models_show_art1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_models',
            name='price',
            field=models.TextField(max_length=50, null=True, verbose_name='Стоимость модели'),
        ),
    ]
