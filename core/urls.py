from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('inquiry.urls'), name='inquiry'),
    path('account/', include('account.urls'), name='account'),
    # JWT API

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


admin.site.index_title = 'Corebuso'
admin.site.site_header = 'COREBUSE'
admin.site.site_title = 'Administration'
