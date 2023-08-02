# pricing_module/admin.py
from django.contrib import admin
from .models import PricingConfig
from .forms import PricingConfigForm

class PricingConfigAdmin(admin.ModelAdmin):
    form = PricingConfigForm

admin.site.register(PricingConfig, PricingConfigAdmin)
