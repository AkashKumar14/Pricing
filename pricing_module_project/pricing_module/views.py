# pricing_module/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal

@csrf_exempt
@require_POST
def calculate_pricing(request):
    data = request.POST
    dbp = Decimal(data.get('dbp', 0))
    dap = Decimal(data.get('dap', 0))
    tmf = Decimal(data.get('tmf', 0))
    wc = Decimal(data.get('wc', 0))
    distance = Decimal(data.get('distance', 0))
    time = Decimal(data.get('time', 0))
    waiting_time = Decimal(data.get('waiting_time', 0))

    additional_distance = distance - 3  # Assuming the first 3 KMs are covered in DBP
    additional_time = time - 60  # Assuming the first 60 minutes are covered in TMF

    if additional_distance > 0:
        distance_cost = additional_distance * dap
    else:
        distance_cost = 0

    if additional_time > 0:
        time_cost = additional_time * tmf
    else:
        time_cost = 0

    total_cost = (dbp + distance_cost) + time_cost + (waiting_time // 3 * wc)

    return JsonResponse({'price': total_cost})

def main_page(request):
    # Add any data you want to pass to the template here
    context = {
        'greeting': 'Hello, welcome to my website!',
    }
    return render(request, 'pricing_module/main_page.html', context)
