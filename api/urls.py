from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short-url/', views.UrlShortener.as_view(), name='short'),
    path('api/v1/qr/', views.GenerateQR.as_view(), name='qr'),
    path('<str:key>/', views.RedirectToUrl.as_view(), name='redirect'),
]