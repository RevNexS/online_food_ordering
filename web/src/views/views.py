from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.
def home(request):
    return redirect('user_login')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required
def dashboard(request : HttpResponse):
    return render(request, 'dashboard/hero.html')