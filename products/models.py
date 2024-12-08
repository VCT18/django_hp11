
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here. 
class Category (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    
class Product (models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE) 
        brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        image = models.ImageField(upload_to='products/')
        price = models. DecimalField(max_digits=10, decimal_places=2)
        new_price = models. DecimalField(max_digits=10, decimal_places=2, default=0)
        on_sale = models.BooleanField(default=False)
        detail = models.TextField(blank=True)
        created_at = models.DateTimeField (auto_created=True)
        
        class Meta:
            ordering = ('name',)
        def __str__(self):
            return self.name


        
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('content',)
    def __str__(self):
        return self.content