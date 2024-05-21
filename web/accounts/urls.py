from django.contrib import admin
from django.urls import path
from .views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login , name='user_login'),
    path('signup/', views.user_signup , name='signup'),
    path('forgot/', views.user_forgot , name='forgot'),
]
