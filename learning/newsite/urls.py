from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.home, name='home'), 
    path("<str:val>", views.action, name='action'),
    path('result/<str:val>/', views.result, name='result')
]