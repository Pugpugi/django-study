from django.db import models

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True , related_name='+')

class Product(models.Model):
    # sku = models.CharField(max_length=10, primary_key= True)  this lets you set primary key
    title = models.CharField(max_length = 255) 
    slug = models.SlugField() # 

    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('Collection', on_delete= models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    # capital means fixed value... DO NOT CHANGE
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_PLATINUM = 'P'
    MEMBERSHIP_DIAMOND = 'D'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE , 'Bronze'),
        (MEMBERSHIP_SILVER , 'Silver'),
        (MEMBERSHIP_GOLD , 'Gold'), 
        (MEMBERSHIP_PLATINUM , 'Platinum'),
        (MEMBERSHIP_DIAMOND , 'Diamond')
    ]

    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length= 255)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length=1, choices= MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed')
    ]

    placed_at = models.DateField(auto_now_add = True)
    payment_status = models.CharField(max_length= 1, choices= PAYMENT_STATUS, default = PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete= models.PROTECT)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255, null=True, default = "")
    # one to one connection
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key= True) 
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
 