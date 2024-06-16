from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.contrib import messages
# from customers.models import CustomerUser , Address
from restaurants.models import RestroUser
# Create your views here.


def restro_signup(request : HttpRequest):
    if request.method == "POST":
        restaurant_name = request.POST['restaurant-name']
        email = request.POST['email']
        password = request.POST['password']
        contact_number = request.POST['contact-number']
        street = request.POST['contact-number']
        city = request.POST['city']
        pin_code = request.POST['pin-code']

        users = RestroUser.objects.filter(email=email)

        if users.exists():
            messages.error(request, 'User exist')
            return render(request, 'restaurants/signup/restaurant_registration.html')

        user = RestroUser.objects.create_user(
            name = restaurant_name,
            email = email,
            password = password,
            contact_number = contact_number,
            street = street,
            city = city,
            pincode = pin_code
        )
        user.save()

        messages.success(request , 'Account Created. Login')
        return redirect('user_login')

    else:
        return render(request, "restaurants/signup/restaurant_registration.html")

def restro_login(request: HttpRequest):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email , password=password)
        if user is not None:
            # messages.success(request , 'Login Successful')
            return redirect('dashboard')
            # return render(request, 'accounts/user_login_page.html')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return render(request , 'accounts/user_login_page.html')
    else:
        return render(request , 'restaurants/login/restro_login_page.html') 
    
