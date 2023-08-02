# pricing_module/tests.py
from django.test import TestCase

class PricingAPITestCase(TestCase):
    def test_calculate_pricing(self):
        data = {
            'dbp': '80',
            'dap': '30',
            'tmf': '1.25',
            'wc': '5',
            'distance': '5',
            'time': '90',
            'waiting_time': '15'
        }
        response = self.client.post('/pricing/calculate_pricing/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['price'], 285.0)
