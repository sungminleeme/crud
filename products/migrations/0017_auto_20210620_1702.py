# Generated by Django 3.2.4 on 2021-06-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_allergy_allergyproduct_image_nutrition_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='english_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='product',
            name='korean_name',
            field=models.CharField(max_length=45),
        ),
    ]