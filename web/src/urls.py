from django.contrib import admin
from django.urls import path
from .views import views
from django.urls import path , include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('accounts/' , include("accounts.urls") , name='accounts'),
]
