from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    featured_products= Product.objects.all().order_by("-priority")[:4]
    latest_products= Product.objects.all().order_by("-id")[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
        
    }
    return render(request,"index.html",context)


def list_product(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    
    page=1
    if request.GET:
        page=request.GET.get('page')
        
        
    product_list= Product.objects.all().order_by("-priority")
    product_paginator = Paginator(product_list,2)
    product_list= product_paginator.get_page(page)
    context={'Products':product_list}
    return render(request,'products.html', context)


def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
        
    return render(request,'product_detail.html', context)



