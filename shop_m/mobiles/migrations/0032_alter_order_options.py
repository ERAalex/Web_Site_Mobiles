# Generated by Django 4.0.3 on 2022-08-09 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0031_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
    ]