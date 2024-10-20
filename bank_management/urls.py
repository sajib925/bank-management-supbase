from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('user.urls')),
    path('api/transactions/', include('transaction.urls')),
    path('api/account/', include('account.urls')),
    path('api/services/', include('service.urls')),
    path('api/contact/', include('contact.urls')),
]
