from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [

    path('dashboard/', Base, name = 'home'),
    path('sign_up/', Sign_up, name = 'signup'),
    path('', Sign_In, name = 'signin'),
    path('logout/', Logout, name = 'logout'),
    path('add_customers/', Addcustomers, name = 'addcustomers'),
    path('add_purchase/', Addpurchase, name = 'addpurchase'),
    path('add_return/', Addreturn, name = 'addreturn'),
    path('add_sale/', Addsale, name = 'addsale'),
    path('add_supplier/', Addsupplier, name = 'addsupplier'),
    path('customers_list/', Listcustomers, name = 'customerlist'),
    path('purchase_list/', Listpurchase, name = 'purchaselist'),
    path('return_list/', Listreturn, name = 'returnlist'),
    path('sale_list/', Listsale, name = 'salelist'),
    path('supplier_list/', Listsupplier, name = 'supplierlist'),
    path('report/', Report, name = 'report'),
    path('error/', Error, name = 'error'),
    path('invoice/', Invoice, name = 'invoice'),
    path('privacy_policy/', Privacy, name = 'privacy'),
    path('terms_of_service/', Terms, name = 'terms'),
    path('stock_summary/', StockSummary, name = 'stocksummary'),
    path('stock_summary_download/', export_stock_summary_to_excel, name = 'export_stock_summary_to_excel'),
    path('deletecustomer/<int:id>', DeleteCustomer, name='deletecustomer'),
    path('deletepurchase/<int:id>', DeletePurchase, name='deletepurchase'),
    path('updatepurchase/<int:id>', UpdatePurchase, name='updatepurchase'),
    path('deletereturn/<int:id>', DeleteReturn, name='deletereturn'),
    path('deletesale/<int:id>', DeleteSale, name='deletesale'),
    path('updatesale/<int:id>', UpdateSale, name='updatesale'),
    path('deletesupplier/<int:id>', DeleteSupplier, name='deletesupplier'),

]