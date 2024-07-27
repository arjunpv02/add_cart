from django.shortcuts import redirect, render
from . models import Order, OrderItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from customers.models import Customer
# Create your views here.


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        customer, created = Customer.objects.get_or_create(user=user)
        
        if created:
            messages.info(request, "Customer profile created.")
        
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        product = Product.objects.get(pk=product_id)
        ordered_item = OrderItem.objects.filter(
            product=product,
            owner=cart_obj
        ).first()

        if ordered_item:
            ordered_item.quantity += quantity
            ordered_item.save()
        else:
            OrderItem.objects.create(
                product=product,
                owner=cart_obj,
                quantity=quantity
            )

        return redirect('cart')



"""def add_to_cart(request):
    if request.POST: 
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        print(cart_obj,created)
        
        product=Product.objects.get(pk=product_id)
        
        # Try to get existing orderitem
        Ordered_item=OrderItem.objects.filter(
            product=product,
            owner=cart_obj
        ).first()
        
        if Ordered_item:
            #if the orderitem exits , update the quantity 
            Ordered_item.quantity=Ordered_item.quantity + quantity
            Ordered_item.save()
        else:
            #If the orderitem not exists, create a new one
            Ordered_item = OrderItem.objects.create(
                product=product,
                owner=cart_obj,
                quantity=quantity
            )
        return redirect('cart')"""


def checkout_cart(request):
    #if request.POST: 
        try:
            user=request.user
            customer = Customer.objects.get(user=user)
            #total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                    order_obj.order_status=Order.ORDER_CONFIRMED
                    order_obj.save()
                    status_message=" YOUR ORDER IS  PROCESSED , it will be delivered soon!"
                    messages.success(request,status_message)
            else:
                    status_message=" UNABLE TO  PROCESS YOUR ORDER !!!"
                    messages.error(request,status_message)
        except Exception as e:
                status_message=" UNABLE TO  PROCESS YOUR ORDER (exception) !!!"
                messages.error(request,status_message)
        return redirect('cart')           
        

def remove_item_from_cart(request,pk):
    item=OrderItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')
    
    

@login_required
def show_cart(request):
    user=request.user
    customer, created = Customer.objects.get_or_create(user=user)
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    
    return render(request,"cart.html",context)


@login_required(login_url="account") 
def view_orders (request):
    user=request.user
    customer=user.customer_profile
    
    return render(request,"cart.html")



@login_required(login_url="account") 
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,"orders.html",context)


@login_required(login_url="account")
def payment(request):
    if request.POST: 
        try:
            user=request.user
            customer = Customer.objects.get(user=user)
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
        except Exception as e:
                
                return redirect('cart')
        

    return render(request,"payment.html")




def cart_m(request):
    return render(request,"cart_m.html")