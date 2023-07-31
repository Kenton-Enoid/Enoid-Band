# Map URLs to view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tour/', views.tour, name='tour'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]