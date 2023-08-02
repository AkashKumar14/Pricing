# pricing_module/models.py
from django.db import models
from django.contrib.auth.models import User

class PricingConfig(models.Model):
    dbp = models.DecimalField(max_digits=10, decimal_places=2, help_text="Distance Base Price")
    dap = models.DecimalField(max_digits=10, decimal_places=2, help_text="Distance Additional Price (per Km)")
    tmf = models.DecimalField(max_digits=5, decimal_places=2, help_text="Time Multiplier Factor")
    wc = models.DecimalField(max_digits=5, decimal_places=2, help_text="Waiting Charges (per 3 minutes)")
    effective_from = models.DateTimeField(help_text="Effective Date & Time for this pricing config")
    enabled = models.BooleanField(default=True, help_text="Whether this pricing config is enabled or not")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_configs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="updated_configs")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pricing Config ({self.effective_from})"
