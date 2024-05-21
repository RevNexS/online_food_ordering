from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest
from customers.models import CustomerUser , Address
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
        f_name = request.POST['first-name']
        l_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['password']
        street = request.POST['street']
        city = request.POST['city']
        pincode = request.POST['pin-code']

        users = CustomerUser.objects.filter(email=email)
        if len(users) > 0 :
            messages.error(request, 'User exist')
            return render(request, 'customers/signup/customer_registration.html')

        user = CustomerUser.objects.create_user(
            first_name = f_name,
            last_name = l_name,
            email = email,
            password = password,
            phone = phone_number
        )
        user.save()

        address = Address.objects.create(
            street_address = street,
            city = city,
            pincode = pincode,
            customer_id = user
        )

        messages.success(request , 'Account Created. Login')
        # return render(request , 'accounts/user_login_page.html')
        return redirect('user_login')
    else:
        return render(request , 'customers/signup/customer_registration.html')
    
def user_forgot(request: HttpRequest):
    pass