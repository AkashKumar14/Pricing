# pricing_module_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pricing_module.urls')),  # Include without a prefix to make it the root URL
    # ... other URL patterns for other apps or views if any ...
]
