from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Infrastructure.service import Facade
from rest_framework import status
# Create your views here.


class CustomerPayment(APIView):
    def get(self,request):
        pass
    def post(self,request):
        # Create User
        request_data = request.data
        
        
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Success",
                "data":request_data
            }
        )
        
        
    def put(self,request):
        pass
    def delete(self,request):
        pass
    

