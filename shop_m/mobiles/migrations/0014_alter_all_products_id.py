# Generated by Django 4.0.3 on 2022-07-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0013_alter_all_products_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
