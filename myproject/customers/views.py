from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer

# Create your views here.


def show_account(request):
    context={}
    if request.method == 'POST':
        if 'register' in request.POST:
            context['register']=True
            try:
                print("request.POST")
                username1=request.POST.get('username')
                email1=request.POST.get('email')
                password1=request.POST.get('password')
                address1=request.POST.get('address')
                phone1=request.POST.get('phone') 
                
                # create user account
                user=User.objects.create_user(
                    username=username1,
                    password=password1,
                    email=email1
                )
                
                # create customer account
                customer = Customer.objects.create(
                name=username1,
                user=user,
                phone=phone1,
                address=address1
                )
                success_message="user registered successfully"
                messages.success('request',success_message)
                
            except Exception as e :
                error_msg=" DUPLICATE USER 0R INVALID INPUTS"
                messages.error(request,error_msg)
    
        elif 'login' in request.POST:
            context['register']=False
            username=request.POST.get('username')
            password=request.POST.get('password')         
            
            user=authenticate(username=username,password=password) 
            
            if user:
                login(request,user) 
                return redirect('home')
            else:
                messages.error(request, 'invalid user credentials' )
        
    return render(request,"account.html",context)


def sign_out(request):
    logout(request)
    return redirect('home')
    
