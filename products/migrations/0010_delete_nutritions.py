# Generated by Django 3.2.4 on 2021-06-20 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nutritions',
        ),
    ]
