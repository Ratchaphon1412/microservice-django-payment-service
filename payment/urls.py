from django.urls import include,path
from rest_framework import routers
from . import views


urlpatterns = [
    path('payment/', views.PaymentApi.as_view()),
    
    
]
