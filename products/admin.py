from django.contrib import admin
from .models import Product # relative import: importing class Product from models.py

# Register your models here.
admin.site.register(Product)
