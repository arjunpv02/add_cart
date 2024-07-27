from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem
from products.models import Product
from customers.models import Customer 
from django.db.models import Sum, F, FloatField, Count, Max, Min, OuterRef , Subquery
from decimal import Decimal
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django.db import models
from django.db.models.functions import Coalesce
from products import views




def admin_dashboard(request):
        # Fetch all orders along with their related items
        orders = Order.objects.all().order_by("-created_at")
        
        # Calculate total sales price by summing all total_price of orders
        total_sales_price = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0.0
        
        # Ensure total_sales_price is a number before multiplication
        if not isinstance(total_sales_price, (int, float)):
            total_sales_price = 0.0

        # Calculate total expenses as 75% of total sales
        total_expenses_price = total_sales_price * 0.75

        # Debugging print statement (can be removed in production)
        print(total_sales_price)
        
        
            
        # Prepare data for the chart
        dates = [DateFormat(order.created_at).format(get_format('DATE_FORMAT')) for order in orders]
        total_prices = [order.total_price for order in orders]
        
        #print(dates, total_prices)
        # Count total users
        total_users = Customer.objects.count()
        
        """# Aggregate product data: number of sales and total price
        product_sales_data = (
        OrderItem.objects
        .values('product__title' , 'product__image')
        .annotate(
            num_sales=Count('id'),
            total_price=Sum(F('quantity') * F('product__price'), output_field=models.FloatField()),
            revenue=Sum(F('quantity') * F('product__price') * 0.3, output_field=FloatField()),  # 30% of total price
            latest_date=Max('owner__created_at') # Latest order date for the product
        )
        .order_by('-num_sales')
        )"""
        
        # Subquery to count order items per product
        order_item_subquery = OrderItem.objects.filter(product=OuterRef('pk')).values('product')
        product_sales_data = Product.objects.annotate(
            num_sales=Coalesce(Subquery(order_item_subquery.annotate(count=Count('id')).values('count')[:1]), 0),
            total_price=Coalesce(Subquery(order_item_subquery.annotate(total=Sum(F('quantity') * F('product__price'), output_field=FloatField())).values('total')[:1]), 0.0),
            revenue=Coalesce(Subquery(order_item_subquery.annotate(rev=Sum(F('quantity') * F('product__price') * 0.3, output_field=FloatField())).values('rev')[:1]), 0.0),
            latest_date=Subquery(order_item_subquery.annotate(latest=Max('owner__created_at')).values('latest')[:1]),
            product_title=F('title'),
            product_image=F('image')
        ).order_by('-num_sales')
        
        print (product_sales_data)
        
        
        context = {
            'orders': orders,
            'total_sales_price':total_sales_price,
            'total_expenses_price':total_expenses_price,
            'total_users':total_users,
            'dates': dates,
            'total_prices': total_prices,
            'product_sales_data': product_sales_data,
        }
        
        return render(request, 'zz_index.html', context)
        
    
def seller_dashboard(request):

        # Fetch all orders along with their related items
        orders = Order.objects.all().order_by("-created_at")
        
        # Calculate total sales price by summing all total_price of orders
        total_sales_price = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0.0
        
        # Ensure total_sales_price is a number before multiplication
        if not isinstance(total_sales_price, (int, float)):
            total_sales_price = 0.0

        # Calculate total expenses as 75% of total sales
        total_expenses_price = total_sales_price * 0.75

        # Debugging print statement (can be removed in production)
        print(total_sales_price)
        
        
            
        # Prepare data for the chart
        dates = [DateFormat(order.created_at).format(get_format('DATE_FORMAT')) for order in orders]
        total_prices = [order.total_price for order in orders]
        
        #print(dates, total_prices)
        # Count total users
        total_users = Customer.objects.count()
        
        """# Aggregate product data: number of sales and total price
        product_sales_data = (
        OrderItem.objects
        .values('product__title' , 'product__image')
        .annotate(
            num_sales=Count('id'),
            total_price=Sum(F('quantity') * F('product__price'), output_field=models.FloatField()),
            revenue=Sum(F('quantity') * F('product__price') * 0.3, output_field=FloatField()),  # 30% of total price
            latest_date=Max('owner__created_at') # Latest order date for the product
        )
        .order_by('-num_sales')
        )"""
        
        # Subquery to count order items per product
        order_item_subquery = OrderItem.objects.filter(product=OuterRef('pk')).values('product')
        product_sales_data = Product.objects.annotate(
            num_sales=Coalesce(Subquery(order_item_subquery.annotate(count=Count('id')).values('count')[:1]), 0),
            total_price=Coalesce(Subquery(order_item_subquery.annotate(total=Sum(F('quantity') * F('product__price'), output_field=FloatField())).values('total')[:1]), 0.0),
            revenue=Coalesce(Subquery(order_item_subquery.annotate(rev=Sum(F('quantity') * F('product__price') * 0.3, output_field=FloatField())).values('rev')[:1]), 0.0),
            latest_date=Subquery(order_item_subquery.annotate(latest=Max('owner__created_at')).values('latest')[:1]),
            product_title=F('title'),
            product_image=F('image')
        ).order_by('-num_sales')
        
        print (product_sales_data)
        
        
        context = {
            'orders': orders,
            'total_sales_price':total_sales_price,
            'total_expenses_price':total_expenses_price,
            'total_users':total_users,
            'dates': dates,
            'total_prices': total_prices,
            'product_sales_data': product_sales_data,
        }
        return render(request,"zz_seller.html",context)
    
    
    
    
    
    
    
    
    
    
'''if request.POST:
    total_orders = Order.objects.count()
    total_sales = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
    total_products = Product.objects.count()
    total_users = User.objects.count()
    recent_orders = Order.objects.select_related('owner').order_by('-created_at')[:10]  # Last 10 orders

    context = {
        'total_orders': total_orders,
        'total_sales': total_sales,
        'total_products': total_products,
        'total_users': total_users,
        'recent_orders': recent_orders,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)  '''
