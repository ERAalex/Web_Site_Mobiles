# Generated by Django 4.0.3 on 2022-08-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0042_remove_all_products_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_products',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка'),
        ),
    ]