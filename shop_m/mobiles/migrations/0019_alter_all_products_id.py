# Generated by Django 4.0.3 on 2022-07-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0018_alter_top_models_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]