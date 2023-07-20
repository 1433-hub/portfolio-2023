from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gagan-hang-limbu-admin/', admin.site.urls),
    path('', include('home.urls')),
]
