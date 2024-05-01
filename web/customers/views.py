from django.shortcuts import render

# Create your views here.
def customer_signup(request):
    customers = Customers.object.all()
    return render(request, 'customer_registration.html', {'customers':customers})
