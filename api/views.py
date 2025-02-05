from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(['GET'])
def number_classifier(request):
    # Extract the 'number' parameter from the query string
    number_param = request.GET.get('number')
    
    # Input validation
    try:
        number = int(number_param)
    except (ValueError, TypeError):
        return Response(
            {"number": number_param, "error": True},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Function to check if a number is prime (only applies to positive integers > 1)
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Function to check if a number is perfect (only applies to positive integers > 0)
    def is_perfect(n):
        if n <= 0:
            return False
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    
    # Function to check if a number is an Armstrong number (only applies to positive integers)
    def is_armstrong(n):
        if n < 0:
            return False
        digits = [int(d) for d in str(abs(n))]
        return sum(d ** len(digits) for d in digits) == abs(n)
    
    # Calculate properties
    digit_sum = sum(int(d) for d in str(abs(number)))  # Use absolute value for digit sum
    properties = []
    
    if number > 0:  # Only check Armstrong for positive numbers
        if is_armstrong(number):
            properties.append("armstrong")
    
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    
    # Prime and perfect checks only apply to positive integers > 1
    if number > 1:
        properties.append("prime" if is_prime(number) else "not_prime")
        properties.append("perfect" if is_perfect(number) else "not_perfect")
    
    # Fetch fun fact from Numbers API (only for non-negative numbers)
    fun_fact = ""
    if number >= 0:
        try:
            fun_fact_response = requests.get(f"http://numbersapi.com/{number}")
            fun_fact = fun_fact_response.text
        except Exception as e:
            fun_fact = f"Unable to fetch fun fact for {number}"
    else:
        fun_fact = "Fun facts are not available for negative numbers."
    
    # Preparing response
    response_data = {
        "number": number,
        "is_prime": is_prime(number) if number > 1 else False,
        "is_perfect": is_perfect(number) if number > 0 else False,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
    
    return Response(response_data, status=status.HTTP_200_OK)