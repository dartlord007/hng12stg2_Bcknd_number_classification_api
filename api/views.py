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

    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to check if a number is perfect
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    # Function to check if a number is an Armstrong number
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        return sum(d ** len(digits) for d in digits) == n

    # Calculate properties
    digit_sum = sum(int(d) for d in str(number))
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    # Fetch fun fact from Numbers API
    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}")
        fun_fact = fun_fact_response.text
    except Exception as e:
        fun_fact = f"Unable to fetch fun fact for {number}"

    # Prepare response
    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }

    return Response(response_data, status=status.HTTP_200_OK)