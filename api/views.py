from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NumberSerializer
from .models import Number
import requests
import math

class NumberClassificationView(APIView):
    def get(self, request):
        number = request.GET.get('number')
        if not number or not number.isdigit():
            return Response({'error': True, 'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

        number = int(number)
        is_prime = self.is_prime(number)
        is_perfect = self.is_perfect(number)
        properties = self.get_properties(number)
        digit_sum = self.get_digit_sum(number)
        fun_fact = self.get_fun_fact(number)

        data = {
            'number': number,
            'is_prime': is_prime,
            'is_perfect': is_perfect,
            'properties': properties,
            'digit_sum': digit_sum,
            'fun_fact': fun_fact
        }

        serializer = NumberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = math.floor(math.sqrt(n))
        for d in range(3, 1 + max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_perfect(self, n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n

    def get_properties(self, n):
        properties = []
        if n % 2 != 0:
            properties.append('odd')
        if n % 2 == 0:
            properties.append('even')
        if self.is_armstrong(n):
            properties.append('armstrong')
        return properties

    def get_digit_sum(self, n):
        return sum(int(digit) for digit in str(n))

    def get_fun_fact(self, n):
        response = requests.get(f'http://numbersapi.com/{n}')
        return response.text

    def is_armstrong(self, n):
        return sum(int(digit) ** len(str(n)) for digit in str(n)) == n