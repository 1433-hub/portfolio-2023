from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name="portfolio"),
    path('portfolio/<slug:slug>/', PortfolioDetailView.as_view(), name="portoflioDetail"),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),
    path('blog-list/', BlogView.as_view(), name='blog'),
    path('type/<slug:slug>', TypeView.as_view(), name="type"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
