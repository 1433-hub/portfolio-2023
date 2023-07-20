from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from home import views

urlpatterns = [
    path('gagan-hang-limbu-admin/', admin.site.urls),
    path('', include('home.urls')),
]

handler500 = views.handler500
handler404 = views.handler404
