from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest

# Create your views here.
def user_login(request: HttpRequest):
    if request.method == 'POST':
        User.objects.get()
    else:
        return render(request , 'accounts/user_login_page.html')