from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

from .models import Inquiry, TestUser
from .serializers import InquirySerializer, TestUserSerializer

""" Q is used for multiple search values """


@api_view(['GET'])
@permission_classes([AllowAny])
def endpoints(request):
    data = [
        '[GET]: /inquiries',
        '[POST]: /inquiry',
        '/subscription',
        '/demo',
        '/inquiry/str:pk',
        '/subscription/str:pk',
        '/demo/str:id',
        '/inquiry/search/?s=str',
        '/user',
        '/user/str:username',
    ]
    return Response(data)


@api_view(['GET'])
def inquiry(request, format=None):
    """Get all inquiries

    Method: GET

    Returns:
        list: All inquiries
    """
    inquiry = Inquiry.objects.all()
    serializer = InquirySerializer(inquiry, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_inquiry(request, format=None):
    """Inquiries from frontend/client

    Method: POST       

    Returns:
        None
    """
    serializer = InquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def inquiry_detail(request, pk, format=None):

    try:
        inquiry = Inquiry.objects.get(pk=pk)
    except Inquiry.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = InquirySerializer(inquiry, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InquirySerializer(inquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        inquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def inquiry_search(request, format=None):
    query = request.GET.get('s')
    if query == None:
        query = ''
    search = Inquiry.objects.filter(
        Q(name__icontains=query) |
        Q(email__icontains=query)
    )
    serializer = InquirySerializer(search, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, format=None):
    user = TestUser.objects.all()
    serializer = TestUserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, username, format=None):
    user = TestUser.objects.get(username=username)
    serializer = TestUserSerializer(user, many=False)
    return Response(serializer.data)
