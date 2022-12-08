from django.urls import path

from . import views

app_name = 'inquiry'

urlpatterns = [
    path('', views.endpoints),
    path('inquiry/', views.inquiry),
    path('inquiry/search/', views.inquiry_search),
    path('inquiry/<str:pk>/', views.inquiry_detail),
    path('user/', views.user, name='user'),
    path('user/<str:username>', views.user_detail, name='user details'),
]
