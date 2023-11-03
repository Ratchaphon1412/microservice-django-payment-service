from django.urls import include,path
from rest_framework import routers
from .views import *


urlpatterns = [
   path('payment/customer/',  CustomerPayment.as_view(), name='payment_customer'),
   path('payment/customer/card/',  CardCustomerPayment.as_view(), name='payment_customer_card'),
   path('payment/',  Payment.as_view(), name='payment_customer_card_list'),
   path('admin/payment/',  AdminPayment.as_view(), name='payment_admin'),
   path('admin/payment/receipt/',  AdminPaymentReceipt.as_view(), name='payment_admin_receipt'),
   path('payment/onetime/',PaymentAnonymous.as_view(),name='payment_anonymous'),
    
    
]
