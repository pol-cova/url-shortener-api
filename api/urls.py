from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short-url/', views.url_shortener, name='short'),
    path('<str:key>/', views.redirect_to_url, name='redirect'),
]