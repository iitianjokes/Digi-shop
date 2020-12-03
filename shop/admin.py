from django.contrib import admin
from shop.models import ProductImage ,Product ,User ,Payment
import math
# Register your models here.

class ProductImageModel(admin.StackedInline):
    model = ProductImage

class ProductModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'get_description' , 'get_price' , 'file',
                    'get_discount','get_saleprice','thumbnail']
    inlines = [ProductImageModel]

    def get_description(self , obj):
        return obj.description[0:15]+'...'

    def get_price(self , obj):
        return 'Rs '+ str(obj.price)

    def get_discount(self , obj):
        return  str(obj.discount) + ' %'

    def get_saleprice(self,obj):
        amount = obj.price - (obj.price * (obj.discount / 100))
        return math.floor(amount)

    get_description.short_description = 'description'
    get_price.short_description = 'price'
    get_discount.short_description = 'discount'
    get_saleprice.short_description = 'sale price'

class UserModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' , 'mobileno' ]
    sortable_by = ['id' , 'name']



admin.site.register(Product , ProductModel)
admin.site.register(User , UserModel)
admin.site.register(Payment)