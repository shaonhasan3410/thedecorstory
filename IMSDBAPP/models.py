from django.db import models

class AddCategory(models.Model):
    image = models.ImageField(upload_to="Category_Image")
    product_name = models.CharField(max_length=25)
    product_category = models.CharField(max_length=25)
    code = models.IntegerField()
    

class AddSale(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product_name = models.CharField(max_length=30, null=True, blank=True)
    product_category = models.CharField(max_length=30, null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    brand_name = models.CharField(max_length=40, null=True, blank=True)
    supplier_name = models.CharField(max_length=40, null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True) #Code Means Purchase ID
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15, null=True, blank=True) #need to be support
    product_color = models.CharField(max_length=12, null=True, blank=True)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    order_quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(blank=True, null=True)
    order_tax = models.IntegerField(null=True, blank=True)
    order_discount = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to="Product_Image", null=True, blank=True)
    total_amount = models.IntegerField(blank=True, null=True) #Need to be support
    sale_status = models.CharField(max_length=20, null=True, blank=True)
    payment_status = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(null=True, blank=True) #Need to be support
    

    def __str__(self):
        return self.product_name

    @property
    def total_price(self):
        return (self.unit_price + (self.unit_price * (self.order_tax / 100))) * self.order_quantity
    
    @property
    def purchase_price(self):
        return self.unit_price * self.order_quantity

    @property
    def saling_price(self):
        return (self.unit_price + (self.unit_price * (self.order_tax / 100)))

    

class AddPurchase(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product_id = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=25, null=True, blank=True)
    product_category = models.CharField(max_length=30, null=True, blank=True)
    brand_name = models.CharField(max_length=30, null=True, blank=True)
    supplier_name = models.CharField(max_length=30, null=True, blank=True)
    product_color = models.CharField(max_length=20, null=True, blank=True)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    product_quantity = models.IntegerField(null=True, blank=True)
    order_tax = models.IntegerField(null=True, blank=True)
    order_discount = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    purchase_status = models.CharField(max_length=20, null=True, blank=True)
    payment_status = models.CharField(max_length=20, null=True, blank=True)
    product_image = models.ImageField(upload_to="Purchase_Image", null=True, blank=True)
    note = models.TextField(null=True, blank=True) #Need to be support
    sale_order_id = models.ForeignKey(AddSale, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name
    


class AddReturn(models.Model):
    date = models.DateField(null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True) #Code Means Purchase ID
    product_name = models.CharField(max_length=25, null=True, blank=True)
    product_category = models.CharField(max_length=30, null=True, blank=True)
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    customer_phone = models.CharField(max_length=30, null=True, blank=True) #Need to be support
    customer_email = models.EmailField(null=True, blank=True)
    order_quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    return_quantity = models.IntegerField(null=True, blank=True)
    return_price = models.IntegerField(null=True, blank=True)
    payment_status = models.CharField(max_length=20, null=True, blank=True)
    note = models.TextField(null=True, blank=True) #Need to be support
    purchase_order_id = models.ForeignKey(AddPurchase, on_delete=models.CASCADE, null=True, blank=True)
    sale_order_id = models.ForeignKey(AddSale, on_delete=models.CASCADE, null=True, blank=True)
    

class AddCustomer(models.Model):
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=30, null=True, blank=True) #Need to be support
    country = models.CharField(max_length=20, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    zip_code= models.PositiveIntegerField(null=True, blank=True)
    customer_type = models.CharField(max_length=30, null=True, blank=True)
    

class AddSupplier(models.Model):
    company_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True) #Need to be support
    contact_person_name = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    zip_code= models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)