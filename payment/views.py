from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Infastructure.service import Facade
# Create your views here.


class PaymentApi(APIView):
    def get(self,request):
        return Response({'Balance':Facade.omiseService().adminBalance()})
    
class CreditCardApi(APIView):
    def get(self,request):
        pass