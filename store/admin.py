from django.contrib import admin
from .models import Category, Product, Banner

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_category', 'is_active')
    list_filter = ('is_active', 'target_category')
    search_fields = ('title',)
