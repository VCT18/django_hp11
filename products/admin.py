from django.contrib import admin
from .models import Category, Product, Comment, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Comment)