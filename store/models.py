from django.db import models

# Create your models here.
    

class Subcategory(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='subcategories/images/')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = "SubCategories"    
    
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    image = models.ImageField(upload_to='categories/images/')
    name = models.CharField(max_length=64)
    subcategory = models.ManyToManyField(Subcategory)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name
    

class Goods(models.Model):
    image = models.ImageField(upload_to='goods/image/')
    name = models.CharField(max_length=124)
    price = models.IntegerField()
    description = models.TextField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name_plural = "Goods"   

        
    def __str__(self):
        return self.name