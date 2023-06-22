from django.contrib import admin
from .models import *


class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('image','product_name','product_category','code')

admin.site.register(AddCategory,AddCategoryAdmin)


class AddSaleAdmin(admin.ModelAdmin):
    list_display = ('date','product_name','product_category','order_id','brand_name','code','customer_name')

admin.site.register(AddSale,AddSaleAdmin)


class AddPurchaseAdmin(admin.ModelAdmin):
    list_display = ('date','product_id','product_name','product_category','brand_name','supplier_name','product_quantity','unit_price','total_price')

admin.site.register(AddPurchase,AddPurchaseAdmin)


class AddReturnAdmin(admin.ModelAdmin):
    list_display = ('date','order_id','product_name','product_category','customer_name','customer_phone','customer_email','return_quantity','return_price')

admin.site.register(AddReturn,AddReturnAdmin)


class AddCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','customer_phone','country','city','zip_code','customer_type')

admin.site.register(AddCustomer,AddCustomerAdmin)


class AddSupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name','email','phone','contact_person_name','city','zip_code','country')

admin.site.register(AddSupplier,AddSupplierAdmin)