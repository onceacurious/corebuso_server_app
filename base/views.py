from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

""" Transfer this code to email app later """


@api_view(['GET'])
@permission_classes([AllowAny])
def endpoints(request):
    data = ['/client', '/account']
    return Response(data)
