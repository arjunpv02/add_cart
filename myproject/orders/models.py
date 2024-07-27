from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

# create model for order
class  Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=(
                (ORDER_CONFIRMED,"ORDER_CONFIRMED"),
                (ORDER_PROCESSED,"ORDER_PROCESSED"),
                (ORDER_DELIVERED,"ORDER_DELIVERED"),
                (ORDER_REJECTED,"ORDER_REJECTED"))
    
    
    # Order  fields
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=1)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id, self.owner.user.username)
    
    
    def calculate_total_price(self):
        # Calculate the total price based on order items
        total = sum(item.quantity * item.product.price for item in self.added_items.all())
        self.total_price = total
        self.save()
    


    
# model for order item ( each order can contains multiple order items)
class OrderItem(models.Model):
    
    
    product=models.ForeignKey(Product,related_name='added_carts', on_delete=models.SET_NULL, null= True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.owner.calculate_total_price()  # Update order total price on save

    def delete(self, *args, **kwargs):
        order = self.owner
        super().delete(*args, **kwargs)
        order.calculate_total_price()  # Update order total price on delete


