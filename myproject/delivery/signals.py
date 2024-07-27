# signals.py in delivery app
from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import OrderItem
from .models import Delivery

@receiver(post_save, sender=OrderItem)
def create_delivery_for_order_item(sender, instance, created, **kwargs):
    if created:
        # Create a Delivery object for the new OrderItem
        delivery = Delivery.objects.create(
            order_item=instance,
            customer=instance.owner.owner,  # Assumes that OrderItem has an 'owner' ForeignKey to Order
            #delivery_address=instance.owner.owner.address,  # Assumes Customer has an 'address' field
        )
        # Add the product to the delivery's product list
        delivery.save()
