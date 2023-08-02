# pricing_module/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('calculate_pricing/', views.calculate_pricing, name='calculate_pricing'),
    # Add other URL patterns for the app if needed
]
