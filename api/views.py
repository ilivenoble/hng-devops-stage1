from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests
#the main view function that will handle the requests
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, abs(n)) if n % i == 0)

def is_armstrong(n):
    num_str = str(abs(n))
    num_len = len(num_str)
    return abs(n) == sum(int(digit) ** num_len for digit in num_str)

def get_fun_fact(number, fact_type='math'):
    response = requests.get(f'http://numbersapi.com/{number}/{fact_type}')
    if response.status_code == 200:
        return response.text
    return "No fun fact available."

@require_GET
def classify_number(request):
    try:
        number = request.GET.get('number')
        if number is None:
            raise ValueError("No number provided")
        number = int(number)
    except (TypeError, ValueError):
        return JsonResponse({"number": request.GET.get('number'), "error": True}, status=400)

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(number))),
        "fun_fact": get_fun_fact(number, 'math')
    }

    return JsonResponse(response_data)