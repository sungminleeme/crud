from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Menu(models.Model):
		name = models.CharField(max_length=50)
class Meta:
          db_table = 'menus' # 테이블 이름


class Category(models.Model):
		name = models.CharField(max_length=20)
		menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Meta:
          db_table = 'categories' # 테이블 이름



class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=6,decimal_places=2)
    sodium_mg =  models.DecimalField(max_digits=6,decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6,decimal_places=2)  
    sugars_g  = models.DecimalField(max_digits=6,decimal_places=2)
    protein_g = models.DecimalField(max_digits=6,decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6,decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'nutritions'    # 테이블 이름       

class Product(models.Model):
    name= models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) 
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE) 


    class Meta:
            db_table = 'products' # 테이블 이름

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Product',on_delete=CASCADE) 

    class Meta:
        db_table = 'images' # 테이블 이름

class Allergy(models.Model):
    name = models.CharField(max_length=20) 
    
    class Meta:
        db_table = 'allergy' # 테이블이름


class Allergyproduct(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE) 
    Product = models.ForeignKey('Product', on_delete=models.CASCADE) 
    
    class Meta:
        db_table =  'allergy_products' # 테이블 이름                    









		