# Generated by Django 4.0.3 on 2022-08-16 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0041_remove_all_products_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_products',
            name='discount',
        ),
    ]