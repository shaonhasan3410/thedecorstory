from django.db import models

class AddCategory(models.Model):
    image = models.ImageField(upload_to="Category_Image")
    product_name = models.CharField(max_length=25)
    product_category = models.CharField(max_length=25)
    code = models.IntegerField()
    

class AddSale(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product_name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30)
    order_id = models.IntegerField()
    brand_name = models.CharField(max_length=40)
    supplier_name = models.CharField(max_length=40)
    code = models.CharField(max_length=15, null=True, blank=True)
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15) #need to be support
    product_color = models.CharField(max_length=12, null=True, blank=True)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    order_quantity = models.IntegerField()
    unit_price = models.IntegerField()
    order_tax = models.IntegerField(null=True, blank=True)
    order_discount = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to="Product_Image", null=True, blank=True)
    total_amount = models.IntegerField() #Need to be support
    sale_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    note = models.TextField(null=True, blank=True) #Need to be support

    def __str__(self):
        return self.product_name

    @property
    def total_price(self):
        return self.unit_price * self.order_quantity

    

class AddPurchase(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=25)
    product_category = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=30)
    supplier_name = models.CharField(max_length=30)
    product_color = models.CharField(max_length=20, null=True, blank=True)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    product_quantity = models.IntegerField()
    order_tax = models.IntegerField()
    order_discount = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField()
    purchase_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to="Purchase_Image", null=True, blank=True)
    note = models.TextField(null=True, blank=True) #Need to be support
    sale_order_id = models.ForeignKey(AddSale, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product_name
    


class AddReturn(models.Model):
    date = models.DateField()
    order_id = models.IntegerField()
    product_name = models.CharField(max_length=25)
    product_category = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=30) #Need to be support
    customer_email = models.EmailField()
    return_quantity = models.PositiveIntegerField()
    return_price = models.PositiveIntegerField(null=True, blank=True)
    payment_status = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(null=True, blank=True) #Need to be support
    

class AddCustomer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=30) #Need to be support
    country = models.CharField(max_length=20)
    billing_address = models.TextField()
    city = models.CharField(max_length=20)
    zip_code= models.PositiveIntegerField()
    customer_type = models.CharField(max_length=30, null=True, blank=True)
    

class AddSupplier(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30) #Need to be support
    contact_person_name = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20)
    zip_code= models.PositiveIntegerField()
    country = models.CharField(max_length=20)