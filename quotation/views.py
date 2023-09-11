from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from Infastructure.service.renderpdf import render_to_pdf
import datetime
# Create your views here.

class QuotationAPIView(APIView):
    def get(self,request):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_number': 1233434,
        }
        pdf = render_to_pdf('ksn/quotation.html', data)
        
        return Response(pdf);
    
    def post(self,request):
        return "hello post"

