# Generated by Django 3.2.4 on 2021-06-20 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_nutrition_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nutrition',
            new_name='Nutri',
        ),
    ]
