from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.endpoints, name='auth-endpoints'),
    path('user-credential/',
         views.frontend_detail, name='user-credential'),
    path('register/', views.register, name='register'),
    path('user-info/<str:username>', views.get_email, name='user-email'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
