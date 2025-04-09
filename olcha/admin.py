from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin,ImportMixin
from olcha.models import Product, Category1, Comment, Category,Attribute,AttributeValue,Images

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product  # Hangi modelni import/export qilishni belgilash

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin1(ImportMixin, admin.ModelAdmin):
    resource_class = ProductResource  # resource sinfini qo'shish

class ProductAdmin2(ExportMixin, admin.ModelAdmin):
    resource_class = ProductResource  # resource sinfini qo'shish


admin.site.register(Product, ProductAdmin1)
admin.site.register(Category1, CategoryAdmin)
admin.site.register(Category,)
admin.site.register(Comment)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Images)
