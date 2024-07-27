from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery, DeliveryStatus
from .forms import DeliveryForm
from orders.models import OrderItem
from django.db.models import F
from django.utils.formats import get_format
from django.utils.dateformat import DateFormat
from orders.models import Order
from customers.models import Customer
from django.db.models import Sum
from products.models import Product
from products import views


def edit_delivery(request, delivery_id):
    # Fetch the Delivery object
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    
    # Access related objects
    order_item = delivery.order_item
    product = order_item.product
    customer = delivery.customer

    # Handle form submission
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            # Redirect to a detailed view after saving
            return redirect('delivery_dashboard')
    else:
        form = DeliveryForm(instance=delivery)
        
        



    # Context data to be passed to the template
    context = {
        'form': form,
        'delivery': delivery,
        'order_item': order_item,
        'product': product,
        'customer': customer,
    }
    
    # Render the edit page
    return render(request, 'edit_delivery.html', context)





def delivery_dashboard(request):
    
    
        # FETCHING DETILS OF THE TOTAL ODERS OF HEAD BAR
        # Fetch all orders along with their related items
    orders = Order.objects.all().order_by("-created_at")
        
        # Calculate total sales price by summing all total_price of orders
    total_sales_price = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0.0
        
        # Ensure total_sales_price is a number before multiplication
    if not isinstance(total_sales_price, (int, float)):
            total_sales_price = 0.0

        # Calculate total expenses as 75% of total sales
    total_expenses_price = total_sales_price * 0.75

        # Prepare data for the chart
    dates = [DateFormat(order.created_at).format(get_format('DATE_FORMAT')) for order in orders]
    total_prices = [order.total_price for order in orders]
        
        #print(dates, total_prices)
        # Count total users
    total_users = Customer.objects.count()
    
    #delivery_item = Delivery.objects.all().order_by('-order_item.owner.created_at')
    
    # Order by the created_at field of the related Order through OrderItem
    delivery_item = Delivery.objects.annotate(
    order_created_at=F('order_item__owner__created_at')  # Assuming order_item -> OrderItem -> owner is the Order model
    ).order_by('-order_created_at')
    
    context = {
        'delivery_item': delivery_item,
        
        'total_prices':total_prices,
        'dates': dates,
        'total_sales_price':total_sales_price,
        'total_expenses_price':total_expenses_price,
        'total_users':total_users,
        
    }
    
    return render(request,'zz_delivery.html',context)