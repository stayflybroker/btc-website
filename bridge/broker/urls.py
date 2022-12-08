from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='broker-home'),
    path('portfolio/', views.portfolio, name='broker-portfolio'),
    path('about/', views.about, name='broker-about'),
    path('deposit/', views.deposit, name='broker-deposit'),
    path('withdraw/', views.withdraw, name='broker-withdraw'),
    path('reviews/', views.reviews, name='broker-reviews'),
    path('done/', views.done, name='broker-done'),
    path('portfolio/', views.portfolio, name='broker-portfolio'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='broker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='broker/logout.html'), name='logout'),
    
]
