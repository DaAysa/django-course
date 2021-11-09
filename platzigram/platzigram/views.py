# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hr')
    return HttpResponse(f'Current time {now}')

def sort_integers(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, not allowed.'
    else:
        message = f'Hello {name}, welcome!'
    return HttpResponse(message)