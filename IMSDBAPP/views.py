from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# shishr code start
import json
from django.http import JsonResponse,HttpResponse
from django.db.models import Max
import os
import pandas as pd
# shishir code end 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import *
from django.db.models import Q
import datetime 
from django.db.models import Sum, F
from .forms import AddPurchaseForm
import random



@login_required(login_url='signin')
def Addcustomers(request):

    message=''
    if request.method == "POST":

        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        country = request.POST.get('country')
        billing_address = request.POST.get('billing_address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        customer_type = request.POST.get('customer_type')

        add_customer = AddCustomer(customer_name=customer_name,customer_email=customer_email,customer_phone=customer_phone,country=country,billing_address=billing_address,city=city,zip_code=zip_code,customer_type=customer_type)
        add_customer.save()

        message="Customer Added Successfully"


    Name = request.user
    return render(request, 'backend/page-add-customers.html', locals())

@login_required(login_url='signin')
def Listcustomers(request):
    customers = AddCustomer.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query != None:
            customers = AddCustomer.objects.filter(Q(customer_phone__icontains=query))
    Name = request.user
    return render(request, 'backend/page-list-customers.html', locals())

def DeleteCustomer(request, id):
    obj = AddCustomer.objects.get(id=id)
    obj.delete()

    return redirect('customerlist')

def Addpurchase(request):

    #message=''
    # shishir code start ------------
    product_id_ = 10000 if AddPurchase.objects.count() == 0 else AddPurchase.objects.aggregate(max=Max('product_id'))["max"]+1
    # shishir code end ------------
    if request.method == "POST":
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        brand_name = request.POST.get('brand_name')
        supplier_name = request.POST.get('supplier_name')
        product_color = request.POST.get('product_color')
        product_size = request.POST.get('product_size')
        product_quantity = request.POST.get('product_quantity')
        order_tax = request.POST.get('order_tax')
        order_discount = request.POST.get('order_discount')
        shipping_charge = request.POST.get('shipping_charge')
        unit_price = request.POST.get('unit_price')
        total_price = request.POST.get('total_price')
        total_price = float(total_price)
        purchase_status = request.POST.get('purchase_status')
        payment_status = request.POST.get('payment_status')
        product_image = request.FILES.get('product_image')
        note = request.POST.get('note')


        try:

            add_purchase = AddPurchase(
                date=date,
                product_id=product_id,
                product_name=product_name,
                product_category=product_category,
                brand_name=brand_name,
                supplier_name=supplier_name,
                product_color=product_color,
                product_size=product_size,
                product_quantity=product_quantity,
                order_tax=order_tax,
                order_discount=order_discount,
                shipping_charge=shipping_charge,
                unit_price=unit_price,
                total_price=total_price,
                purchase_status=purchase_status,
                payment_status=payment_status,
                product_image=product_image,
                note=note
                )
            add_purchase.save()

            error = "no"
        except:
            error="yes"

    #message="Purchase Added Successfully"


    Name = request.user
    return render(request, 'backend/page-add-purchase.html', locals())

@login_required(login_url='signin')
def Listpurchase(request):
    purchases = AddPurchase.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query != None:
            purchases = AddPurchase.objects.filter(Q(product_id__icontains=query))
    Name = request.user
    return render(request, 'backend/page-list-purchase.html', locals())

def DeletePurchase(request, id):
    obj = AddPurchase.objects.get(id=id)
    obj.delete()

    return redirect('purchaselist')

def UpdatePurchase(request, id):
    product = AddPurchase.objects.get(id=id)
    if request.method == "POST":
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        brand_name = request.POST.get('brand_name')
        supplier_name = request.POST.get('supplier_name')
        product_color = request.POST.get('product_color')
        product_size = request.POST.get('product_size')
        product_quantity = request.POST.get('product_quantity')
        order_tax = request.POST.get('order_tax')
        order_discount = request.POST.get('order_discount')
        shipping_charge = request.POST.get('shipping_charge')
        unit_price = request.POST.get('unit_price')
        total_price = request.POST.get('total_price')
        total_price = float(total_price)
        purchase_status = request.POST.get('purchase_status')
        payment_status = request.POST.get('payment_status')
        product_image = request.FILES.get('product_image')
        note = request.POST.get('note')

        if product_image == None:
            update_purchase = AddPurchase(id=id,
                    date=date,
                    product_id=product_id,
                    product_name=product_name,
                    product_category=product_category,
                    brand_name=brand_name,
                    supplier_name=supplier_name,
                    product_color=product_color,
                    product_size=product_size,
                    product_quantity=product_quantity,
                    order_tax=order_tax,
                    order_discount=order_discount,
                    shipping_charge=shipping_charge,
                    unit_price=unit_price,
                    total_price=total_price,
                    purchase_status=purchase_status,
                    payment_status=payment_status,
                    product_image=product.product_image,
                    note=note
                    )
            update_purchase.save()
            return redirect("purchaselist")
        else:
            update_purchase = AddPurchase(id=id,
                    date=date,
                    product_id=product_id,
                    product_name=product_name,
                    product_category=product_category,
                    brand_name=brand_name,
                    supplier_name=supplier_name,
                    product_color=product_color,
                    product_size=product_size,
                    product_quantity=product_quantity,
                    order_tax=order_tax,
                    order_discount=order_discount,
                    shipping_charge=shipping_charge,
                    unit_price=unit_price,
                    total_price=total_price,
                    purchase_status=purchase_status,
                    payment_status=payment_status,
                    product_image=product_image,
                    note=note
                    )
            update_purchase.save()
            return redirect("purchaselist")
    
    return render(request, 'backend/update-add-purchase.html', locals())

def UpdateSale(request, id):
    product = AddSale.objects.get(id=id)
    if request.method == "POST":
        date = request.POST.get('date')
        customer_phone = request.POST.get('customer_phone')
        order_id = request.POST.get('order_id')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        brand_name = request.POST.get('brand_name')
        supplier_name = request.POST.get('supplier_name')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        product_color = request.POST.get('product_color')
        product_size = request.POST.get('product_size')
        stock_quantity = request.POST.get('stock_quantity')
        order_quantity = request.POST.get('order_quantity')
        unit_price = request.POST.get('unit_price')
        order_tax = request.POST.get('order_tax')
        order_discount = request.POST.get('order_discount')
        shipping_charge = request.POST.get('shipping_charge')
        total_amount = request.POST.get('total_amount')
        product_image = request.FILES.get('product_image')
        sale_status = request.POST.get('sale_status')
        payment_status = request.POST.get('payment_status')
        billing_address = request.POST.get('billing_address')
        shipping_address = request.POST.get('shipping_address')
        note = request.POST.get('note')

        if product_image == None:
            update_sale = AddSale(id=id,
                    date=date,
                    customer_phone=customer_phone,
                    order_id=order_id,
                    product_name=product_name,
                    product_category=product_category,
                    brand_name=brand_name,
                    supplier_name=supplier_name,
                    customer_name=customer_name,
                    customer_email=customer_email,
                    product_color=product_color,
                    product_size=product_size,
                    stock_quantity=stock_quantity,
                    order_quantity=order_quantity,
                    unit_price=unit_price,
                    order_tax=order_tax,
                    order_discount=order_discount,
                    shipping_charge=shipping_charge,
                    total_amount=total_amount,
                    product_image=product.product_image,
                    sale_status=sale_status,
                    payment_status=payment_status,
                    billing_address=billing_address,
                    shipping_address=shipping_address,
                    note=note
                    )
            update_sale.save()
            return redirect("salelist")
        else:
            update_sale = AddSale(id=id,
                    date=date,
                    customer_phone=customer_phone,
                    order_id=order_id,
                    product_name=product_name,
                    product_category=product_category,
                    brand_name=brand_name,
                    supplier_name=supplier_name,
                    customer_name=customer_name,
                    customer_email=customer_email,
                    product_color=product_color,
                    product_size=product_size,
                    stock_quantity=stock_quantity,
                    order_quantity=order_quantity,
                    unit_price=unit_price,
                    order_tax=order_tax,
                    order_discount=order_discount,
                    shipping_charge=shipping_charge,
                    total_amount=total_amount,
                    product_image=product_image,
                    sale_status=sale_status,
                    payment_status=payment_status,
                    billing_address=billing_address,
                    shipping_address=shipping_address,
                    note=note
                    )
            update_sale.save()
            return redirect("salelist")
    
    return render(request, 'backend/update-add-sale.html', locals())

@login_required(login_url='signin')
def Addreturn(request):

    #Product Id Wise Lookup --------------------- Start
    lookupCode = request.GET.get('order_id')
    try:
        if lookupCode:
            category = AddSale.objects.get(order_id=lookupCode)
            product_id = category.product_id
            product_name = category.product_name
            product_category = category.product_category
            customer_name = category.customer_name
            customer_phone = category.customer_phone
            customer_email = category.customer_email
            order_quantity = category.order_quantity
            order_discount = category.order_discount
            payment_status = category.payment_status

            response_data = {
                'status': 'success',
                'product_id': product_id,
                'product_name': product_name,
                'product_category': product_category,
                'customer_name': customer_name,
                'customer_phone': customer_phone,
                'customer_email': customer_email,
                'order_quantity': order_quantity,
                'order_discount': order_discount,
                'payment_status': payment_status,
            }
            return JsonResponse(response_data)
    except Exception as e:
        response_data = {
                'status': 'failed'
            }
        return JsonResponse(response_data)
    
    #lookup --------------------- End
   

    message=''
    if request.method == "POST":

        date = request.POST.get('date')
        order_id = request.POST.get('order_id')
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        order_quantity = request.POST.get('order_quantity')
        return_quantity = request.POST.get('return_quantity')
        return_price = request.POST.get('return_price')
        payment_status = request.POST.get('payment_status')
        note = request.POST.get('note')

        add_return = AddReturn(
            date=date,
            order_id=order_id,
            product_id=product_id,
            product_name=product_name,
            product_category=product_category,
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_email=customer_email,
            order_quantity=order_quantity,
            return_quantity=return_quantity,
            return_price=return_price,
            payment_status=payment_status,
            note=note
            )
        add_return.save()
        sale_return = AddSale.objects.get(order_id=order_id)
        current_quantity = sale_return.order_quantity
        new_quantity = int(current_quantity) - int(return_quantity)
        sale_return.order_quantity = new_quantity

        current_amount = sale_return.order_discount
        amount = int(sale_return.unit_price) * int(return_quantity)
        new_amount = int(current_amount) - int(amount)
        sale_return.order_discount = new_amount
        sale_return.save()

        purchsae_return = AddPurchase.objects.get(product_id=product_id)
        current_quantity = purchsae_return.product_quantity
        new_quantity = int(current_quantity) + int(return_quantity)
        purchsae_return.product_quantity = new_quantity

        amounts = int(purchsae_return.unit_price) * int(return_quantity)
        current_amount = purchsae_return.total_price
        new_amounts = int(current_amount) + int(amounts)
        purchsae_return.total_price = new_amounts
        purchsae_return.save()

        # return JsonResponse({'status':'success','new_stock_quantity':new_quantity})

    #message="Return Product Added Successfully"


    Name = request.user
    return render(request, 'backend/page-add-return.html', locals())

@login_required(login_url='signin')
def Listreturn(request):
    returns = AddReturn.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query != None:
            returns = AddReturn.objects.filter(Q(order_id__icontains=query))
    Name = request.user
    return render(request, 'backend/page-list-returns.html', locals())

def DeleteReturn(request, id):
    obj = AddReturn.objects.get(id=id)
    obj.delete()

    return redirect('returnlist')

def Addsale(request):

    #message=''

    #Product Id Wise Lookup --------------------- Start
    try:
        lookupCode = request.GET.get('product_id')
        if lookupCode:
            category = AddPurchase.objects.get(product_id=lookupCode)
            product_name = category.product_name
            product_category = category.product_category
            brand_name = category.brand_name
            product_color = category.product_color
            product_size = category.product_size
            supplier_name = category.supplier_name
            product_quantity = category.product_quantity
            unit_price = category.unit_price
            product_image = category.product_image.url
            
            response_data = {
                'status': 'success',
                'product_name': product_name,
                'product_category': product_category,
                'brand_name': brand_name,
                'product_color': product_color,
                'product_size': product_size,
                'supplier_name': supplier_name,
                'product_quantity':product_quantity,
                'unit_price':unit_price,
                'product_image':product_image
            }
            return JsonResponse(response_data)
    except Exception as e:
        response_data = {
                'status': 'failed'
            }
        return JsonResponse(response_data)
    
    #lookup --------------------- End

    # Phone Number Wise Lookup --------------------- Start
    
    try:
        lookupphone = request.GET.get('customer_phone')
        if lookupphone:
            category = AddCustomer.objects.get(customer_phone=lookupphone)
            customer_name = category.customer_name
            customer_email = category.customer_email
            billing_address = category.billing_address
            
            response_data = {
                'status': 'success',
                'customer_name': customer_name,
                'customer_email': customer_email,
                'billing_address': billing_address
            }
            return JsonResponse(response_data)
    except Exception as e:
        response_data = {
                'status': 'failed'
            }
        return JsonResponse(response_data)
    
    # Phone lookup --------------------- End

    order_id_ = 1 if AddSale.objects.count() == 0 else AddSale.objects.aggregate(max=Max('order_id'))["max"]+1



    if request.method == "POST":
        date = request.POST.get('date')
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        order_id = request.POST.get('order_id')
        brand_name = request.POST.get('brand_name')
        supplier_name = request.POST.get('supplier_name')
        product_id = request.POST.get('product_id')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        product_color = request.POST.get('product_color')
        product_size = request.POST.get('product_size')
        stock_quantity = request.POST.get('stock_quantity')
        order_quantity = request.POST.get('order_quantity')
        unit_price = request.POST.get('unit_price')
        order_tax = request.POST.get('order_tax')
        order_discount = request.POST.get('order_discount')
        shipping_charge = request.POST.get('shipping_charge')
        billing_address = request.POST.get('billing_address')
        shipping_address = request.POST.get('shipping_address')
        total_amount = request.POST.get('total_amount')
        total_amount = float(total_amount)
        sale_status = request.POST.get('sale_status')
        payment_status = request.POST.get('payment_status')
        note = request.POST.get('note')
        purchase_image = AddPurchase.objects.get(product_id=product_id)
        add_saledata = AddSale(
                date=date,
                product_name=product_name,
                product_category=product_category,
                order_id=order_id,
                brand_name=brand_name,
                supplier_name=supplier_name,
                product_id=product_id,
                customer_name=customer_name,
                customer_email=customer_email,
                customer_phone=customer_phone,
                product_color=product_color,
                product_size=product_size,
                stock_quantity=stock_quantity,
                order_quantity=order_quantity,
                unit_price=unit_price,
                order_tax=order_tax,
                order_discount=order_discount,
                shipping_charge=shipping_charge,
                billing_address=billing_address,
                shipping_address=shipping_address,
                product_image=purchase_image.product_image,
                total_amount=total_amount,
                sale_status=sale_status,
                payment_status=payment_status,
                note=note
                )
        add_saledata.save()
        purchase = AddPurchase.objects.get(product_id=product_id) # Code Means Purchase ID
        current_quantity = purchase.product_quantity
        current_total = purchase.total_price
        new_quantity = int(current_quantity) - int(order_quantity)
        new_total = int(current_total) - int(order_discount) # "order_discount" is a Total Payment Amount
        purchase.product_quantity = new_quantity
        purchase.total_price = new_total  
        purchase.save()

        return JsonResponse({'status':'success','new_stock_quantity':new_quantity})

    #message="Sales Added Successfully"


    
    Name = request.user
    return render(request, 'backend/page-add-sale.html', locals())
@login_required(login_url='signin')
def Listsale(request):
    sales = AddSale.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query != None:
            sales = AddSale.objects.filter(Q(order_id__icontains=query))

    Name = request.user
    return render(request, 'backend/page-list-sale.html', locals())

def DeleteSale(request, id):
    obj = AddSale.objects.get(id=id)
    obj.delete()

    return redirect('salelist')

@login_required(login_url='signin')
def Addsupplier(request):

    message=''
    if request.method == "POST":

        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact_person_name = request.POST.get('contact_person_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')

        add_supplier = AddSupplier(company_name=company_name,email=email,phone=phone,contact_person_name=contact_person_name,address=address,city=city,zip_code=zip_code,country=country)
        add_supplier.save()

        message="Supplier Added Successfully"


    Name = request.user
    return render(request, 'backend/page-add-supplier.html', locals())

@login_required(login_url='signin')
def Listsupplier(request):
    suppliers = AddSupplier.objects.all()
    if request.method == "GET":
        query = request.GET.get('query')
        if query != None:
            suppliers = AddSupplier.objects.filter(Q(company_name__icontains=query))
    Name = request.user
    return render(request, 'backend/page-list-suppliers.html', locals())

def DeleteSupplier(request, id):
    obj = AddSupplier.objects.get(id=id)
    obj.delete()

    return redirect('supplierlist')

@login_required(login_url='signin')
def Report(request):

    Name = request.user
    stock_report = AddPurchase.objects.all()
    sale_stock = AddSale.objects.filter(payment_status="Due")

# Calculate Daily Sale Start
    sales = AddSale.objects.all()
    
    dataset = []
    for i in sales:
        dataset.append({'date':i.date.strftime("%Y-%m-%d"),'total':i.order_discount})

    totals = {}

    for item in dataset:
        date = item['date']
        total = item['total']
        if date in totals:
            totals[date] += total
        else:
            totals[date] = total

    dataset = [{'date': date, 'total': total} for date, total in totals.items()]

# Calculate Daily Sale End

# Low Stock Qty Summary Start---    

    # Define the threshold value for low stock quantity
    low_quantity_threshold = 5
    
    # Calculate the grouped stock with total quantity and amount
    low_stock = stock_report.values('product_name').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('total_product_quantity')
    
    # Add additional field for low stock quantity
    for group in low_stock:
        group['is_low_quantity'] = group['total_product_quantity'] < low_quantity_threshold

# Low Stock Summary End

    # Customer Name Wise Summary Start
    customer_due = sale_stock.values('customer_name').annotate(
        total_order_quantity=Sum('order_quantity'),
        total_order_amount=Sum('total_amount'),
    ).order_by('total_order_amount')
    # Customer Name Wise Summary End

    # supplier Name Wise Start
    supplier_stock = stock_report.values('supplier_name').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('supplier_name')
    # Supplier Name Wise End

    # Category Name Wise Start
    category_stock = stock_report.values('product_category').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('product_category')
    # Category Name Wise End

    # Product Name Wise Stock Summary Start
    grouped_stock = stock_report.values('product_name', "product_category", "brand_name", 'supplier_name', 'product_color', 'product_size').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('product_name')
    # Product Name Wise Stock Summary End

    return render(request, 'backend/page-report.html', locals())

def Error(request):
    Name = request.user
    return render(request, 'backend/pages-error.html', locals())

@login_required(login_url='signin')
def Invoice(request):
    Name = request.user
    # # Random number generator start
    # char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # num = "0123456789"
    # string = char + num
    # length = 4
    # random_num = "".join(random.sample(string, length))
    # # rRandom number generator end

    
    try:
        order_id = request.GET.get("order_id")
        orders = AddSale.objects.filter(order_id=order_id)
        # orders = AddSale.objects.get(id=order_id)

        date = dict()
        for unique in orders:
            if unique.date in date:
                date[unique.date] += 1
            else:
                date[unique.date] = 1
        
        total_price = dict()
        for unique in orders:
            if unique.total_price in total_price:
                total_price[unique.total_price] += 1
            else:
                total_price[unique.total_price] = 1
        
        shipping_address = dict()
        for unique in orders:
            if unique.shipping_address in shipping_address:
                shipping_address[unique.shipping_address] += 1
            else:
                shipping_address[unique.shipping_address] = 1

        customer_name = dict()
        for unique in orders:
            if unique.customer_name in customer_name:
                customer_name[unique.customer_name] += 1
            else:
                customer_name[unique.customer_name] = 1

        sale_status = dict()
        for unique in orders:
            if unique.sale_status in sale_status:
                sale_status[unique.sale_status] += 1
            else:
                sale_status[unique.sale_status] = 1

        note = dict()
        for unique in orders:
            if unique.note in note:
                note[unique.note] += 1
            else:
                note[unique.note] = 1


        payment_status = dict()
        for unique in orders:
            if unique.payment_status in payment_status:
                payment_status[unique.payment_status] += 1
            else:
                payment_status[unique.payment_status] = 1


        customer_phone = dict()
        for unique in orders:
            if unique.customer_phone in customer_phone:
                customer_phone[unique.customer_phone] += 1
            else:
                customer_phone[unique.customer_phone] = 1


        date_ = list(date.keys())[0]
        shipping_address_ = list(shipping_address.keys())[0]
        customer_name = list(customer_name.keys())[0]
        sale_status = list(sale_status.keys())[0]
        total_price = list(total_price.keys())[0]
        note = list(note.keys())[0]
        payment_status = list(payment_status.keys())[0]
        customer_phone = list(customer_phone.keys())[0]
        print(shipping_address)
        print(orders)


        # get total 
        total = 0
        for i in orders:
            print(i.order_discount) # "order_discount" is total Payment Amount
            total = total + i.order_discount #"order_discount" is total Payment Amount

        # get total 
        due = 0
        for i in orders:
            print(i.total_amount)
            due = due + i.total_amount

        shipping_charge = 0
        for i in orders:
            print(i.shipping_charge)
            shipping_charge = shipping_charge + i.shipping_charge
        
        # Calculate total
        totals = 0
        for i in orders:
            totals += i.unit_price * i.order_quantity
    except:
        pass
    return render(request, 'backend/pages-invoice.html', locals())

@login_required(login_url='signin')
def StockSummary(request):
    Name = request.user
    stock_summary = AddPurchase.objects.all()
    return render(request, 'backend/stock_summary.html', locals())

def export_stock_summary_to_excel(request):
    try:
        stock_summery = AddPurchase.objects.all()
        data = []
        for i in stock_summery:
            data.append({
                "Purchase Date": i.date,
                "Product Id": i.product_id,
                "Product Name": i.product_name,
                "Product Category": i.product_category,
                "Brand Name": i.brand_name,
                "Supplier Name": i.supplier_name,
                "Stock Quantity": i.product_quantity,
                "Stock Amount": i.total_price,
            })


        df = pd.DataFrame(data)
        filepath = "media/stock_summary.xlsx" 
        df.to_excel(filepath, index=False)
        file_location = os.path.abspath(filepath)
        if file_location:
            return redirect("/media/stock_summary.xlsx")
        return redirect("stocksummary")
    except Exception as e:
        return JsonResponse({
            'status': 500,
            'message': f'An error occurred: {str(e)}'
        })


def Sign_up(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        checkbox = request.POST.get('checkbox', False)

        if password != password1:
            error_message = 'Passwords do not match.'
            return render(request, 'backend/auth_sign_up.html', {'error_message': error_message})
        
        if not checkbox:
            error_message = 'You must accept the terms and conditions.'
            return render(request, 'backend/auth_sign_up.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=name, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('signin')   
    return render(request, 'backend/auth_sign_up.html')

def Sign_In(request):
    if request.method == "POST":

        name = request.POST['name']
        password = request.POST['password']
        remember = request.POST.get('remember', False)
        
        user = authenticate(username=name, password=password)
        login(request, user)

        return redirect('home')
    return render(request, 'backend/auth-sign-in.html')

@login_required(login_url='signin')
def Logout(request):
    logout(request)
    return redirect('signin')


def Privacy(request):
    return render(request, 'backend/privacy-policy.html')

def Terms(request):
    return render(request, 'backend/terms-of-service.html')

def get_greeting():
    current_time = datetime.datetime.now().time()
    noon_start = datetime.time(12, 0)
    evening_start = datetime.time(17, 0)
    night_start = datetime.time(20, 0)

    if current_time < noon_start:
        return 'Good Morning'
    elif current_time < evening_start:
        return 'Good Afternoon'
    elif current_time < night_start:
        return 'Good Noon'
    else:
        return 'Good Night'

@login_required(login_url='signin')
def Base(request):
    greeting = get_greeting()
    name = request.user

    top_product = AddSale.objects.all()

    Name = request.user
    stock_report = AddPurchase.objects.all()
    sale_stock = AddSale.objects.filter(payment_status="Due")

# Calculate Daily Sale Start
    sales = AddSale.objects.all()
    dataset = []
    for i in sales:
        dataset.append({'date':i.date.strftime("%Y-%m-%d"),'total':i.order_discount})

    totals = {}

    for item in dataset:
        date = item['date']
        total = item['total']
        if date in totals:
            totals[date] += total
        else:
            totals[date] = total

    dataset = [{'date': date, 'total': total} for date, total in totals.items()]

# Calculate Daily Sale End

# Low Stock Qty Summary Start---    

    # Define the threshold value for low stock quantity
    low_quantity_threshold = 5
    
    # Calculate the grouped stock with total quantity and amount
    low_stock = stock_report.values('product_name').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('total_product_quantity')
    
    # Add additional field for low stock quantity
    for group in low_stock:
        group['is_low_quantity'] = group['total_product_quantity'] < low_quantity_threshold

# Low Stock Summary End

    # Customer Name Wise Summary Start
    customer_due = sale_stock.values('customer_name').annotate(
        total_order_quantity=Sum('order_quantity'),
        total_order_amount=Sum('total_amount'),
    ).order_by('total_order_amount')
    # Customer Name Wise Summary End

    # supplier Name Wise Start
    supplier_stock = stock_report.values('supplier_name').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('supplier_name')
    # Supplier Name Wise End

    # Category Name Wise Start
    category_stock = stock_report.values('product_category').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('product_category')
    # Category Name Wise End

    # Product Name Wise Stock Summary Start
    grouped_stock = stock_report.values('product_name').annotate(
        total_product_quantity=Sum('product_quantity'),
        total_price=Sum('total_price')
    ).order_by('product_name')
    # Product Name Wise Stock Summary End


    total_order_qty = AddSale.objects.aggregate(total_qty=Sum('order_quantity'))['total_qty']
    total_order_amount = AddSale.objects.aggregate(order_discount=Sum('order_discount'))['order_discount']
    unit_price = AddSale.objects.aggregate(unit_price=Sum('unit_price'))['unit_price']
    order_quantity = AddSale.objects.aggregate(order_quantity=Sum('order_quantity'))['order_quantity']
    shipping_charge = AddSale.objects.aggregate(shipping_charge=Sum('shipping_charge'))['shipping_charge']
    total_purchase_cost = AddPurchase.objects.aggregate(total_cost=Sum('total_price'))['total_cost']
    order_price = unit_price * order_quantity
    order_price_with_ship = order_price + shipping_charge

    profit_margin = total_order_amount - order_price_with_ship

    return render(request, 'index.html', locals())

