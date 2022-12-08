from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

""" Transfer this code to email app later """


@api_view(['GET'])
def endpoints(request):
    data = ['/client', '/account']
    return Response(data)
