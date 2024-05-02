from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest
from customers.models import CustomerUser
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def user_login(request: HttpRequest):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email , password=password)
        if user is not None:
            messages.success(request , 'Login Successful')
            return render(request, 'accounts/user_login_page.html')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return render(request , 'accounts/user_login_page.html')
    else:
        return render(request , 'accounts/user_login_page.html')
    

def user_signup(request: HttpRequest):
    if request.method == 'POST':
        f_name = ''
        l_name = ""
        email = ''
        password = ''
        phone_number = ''
        street = ''
        city = ''
        pincode = ''
        
        print()
    else:
        return render(request , 'customers/signup/customer_registration.html')
    
def user_forgot(request: HttpRequest):
    pass