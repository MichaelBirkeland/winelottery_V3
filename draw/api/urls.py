from django.urls import path, include
from django.contrib import admin
from .views import TicketsAPIView


urlpatterns=[
    path('', TicketsAPIView.as_view(), name='API_tickets'),
]
