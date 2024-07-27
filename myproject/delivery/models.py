from django.db import models
from orders.models import Order,OrderItem
from customers.models import Customer
from products.models import Product

# Create your models here.

class DeliveryStatus:
    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'
    CHOICES = [
        (PENDING, 'Pending'),
        (IN_TRANSIT, 'In Transit'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]


class Delivery(models.Model):
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE, related_name='delivery')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='deliveries')
    status = models.CharField(max_length=50, choices=DeliveryStatus.CHOICES, default=DeliveryStatus.PENDING)
    delivery_address = models.TextField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Delivery for Order {self.order.id} - {self.status}'