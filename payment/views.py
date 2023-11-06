from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Infrastructure.service import Facade
from rest_framework import status
from payment.serializers import *
from django.conf import settings
from payment.models import *

import requests
import json

from payment.models import *
from django.contrib.auth.models import User
# Create your views here.


class CustomerPayment(APIView):
    def get(self,request):
        pass
    def post(self,request):
        serializer = CustomerPaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_service = Facade.omiseService()
            customer = payment_service.createCustomer(serializer.validated_data['email'],serializer.validated_data['description'])
            return Response({"customer": customer}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def put(self,request):
        customer_token = request.data.get('customer_token')
        card_token = request.data.get('card_token')
        
        if not customer_token:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not card_token:
            return Response({"error": "card_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_service = Facade.omiseService()
        
        customer_card = payment_service.addCardCustomer(customer_token,card_token)
        
        return Response({"customer_card": "Success Add Card"}, status=status.HTTP_200_OK)
        
        
    
    
    def delete(self,request):
        token = request.data.get('customer_token')
        
        if token == None:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payment_service = Facade.omiseService()
            customer = payment_service.deleteCustomer(token)
        except Exception as e:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response({"message": "Delete Customer Payment Success"}, status=status.HTTP_200_OK)
        
        
        
class CardCustomerPayment(APIView):
    def get(self,request):
        token = request.GET.get('token')
        payment_service = Facade.omiseService()
        listCard = payment_service.listCustomerCard(token)
        print(listCard)
        
        
        return Response({"listCard": listCard}, status=status.HTTP_200_OK)
        
        
        
    def put(self,request):
        customer_id = request.data.get('customer_token')
        card_id = request.data.get('card_token')
       
        
        if not customer_id:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not card_id:
            return Response({"error": "card_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
  
        
        # TODO: Validate customer_id, card_id, and amount
        
        payment_service = Facade.omiseService()
        charge = payment_service.addCardCustomer(customer_id,card_id)
        
        return Response({"message":"Success Add Card Customer"}, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer =  CardCustomerPaymentSerializer(data=request.data)
        
        if serializer.is_valid():
            payment_service = Facade.omiseService()
            token_card = payment_service.createCard(serializer.validated_data['name'],serializer.validated_data['number'],serializer.validated_data['expiration_month'],serializer.validated_data['expiration_year'],serializer.validated_data['city'],serializer.validated_data['postal_code'],serializer.validated_data['security_code'])
            return Response({"token_card": token_card}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        customer_id = request.data.get('customer_token')
        card_id = request.data.get('card_token')
       
        
        if not customer_id:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not card_id:
            return Response({"error": "card_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        payment_service = Facade.omiseService()
        response = payment_service.deleteCustomerCard(customer_id,card_id)
        # api = Facade.apiService()
        # url = f"https://api.omise.co/customers/{customer_id}/cards/{card_id}"
        # headers = {
        #     "Authorization": f"Bearer {settings.OMISE_SECRETE}",
        # }
        # response = api.delete(url,{},headers)
        # url = f'https://api.omise.co/customers/{customer_id}/cards/{card_id}'
        # headers = {
        #     "Authorization": f"Bearer {settings.OMISE_SECRETE}:",
        # }
        # response = requests.delete(url,headers=headers)
        
        
        return Response({"card":"Delete Card Success"}, status=status.HTTP_200_OK)
    
class Payment(APIView):
    def post(self,request):
        customer_id = request.data.get('customer_token')
        card_id = request.data.get('card_token')
        amount = request.data.get('amount')
    
        
        if not customer_id:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not card_id:
            return Response({"error": "card_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not amount:
            return Response({"error": "amount not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_service = Facade.omiseService()
        pay = payment_service.paymentCardRegister(customer_id,card_id,amount,settings.OMISE_RETURN_URI)
        
        return Response({"message": "Success Payment"}, status=status.HTTP_200_OK)
        

class PaymentAnonymous(APIView):
    def post(self,request):
        token = request.data.get('token')
        amount = request.data.get('amount')
    
        
        if not token:
            return Response({"error": "token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not amount:
            return Response({"error": "amount not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_service = Facade.omiseService()
        pay = payment_service.paymentCardOnetime(amount,token,settings.OMISE_RETURN_URI)
        
        return Response({"message": "Success Payment"}, status=status.HTTP_200_OK)


class PaymentPromptPay(APIView):
    def post(self,request):
        amount = request.data.get('amount')
    
        
        if not amount:
            return Response({"error": "amount not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_service = Facade.promptpayService()
        pay = payment_service.qrcode(amount)
        
        return Response({"qrcode":settings.BASE_URL + settings.MEDIA_URL+'qrcode/'+pay}, status=status.HTTP_200_OK)

class AdminPayment(APIView):
    def get(self,request):
        payment_service = Facade.omiseService()
        balance = payment_service.adminBalance()
        
        
        
        return Response({"balance": balance}, status=status.HTTP_200_OK)
        
        
class AdminPaymentReceipt(APIView):
    def get(self,request):
        payment_service = Facade.omiseService()
        receipts = payment_service.adminReceipt()
       
        
        
        
        return Response({"receipts": receipts}, status=status.HTTP_200_OK)
    
    def post(self,request):
        receipt_id = request.data.get('receipt_id')
        payment_service = Facade.omiseService()
        receipt = payment_service.adminReceiptDetail(receipt_id)
        
       
        
        
        
        return Response({"receipts": receipt}, status=status.HTTP_200_OK)
    
        
class  PaymentInvoice(APIView):
    def post(self,request):
        customer_id = request.data.get('user_id')
        amount = request.data.get('amount')
        pdf = request.data.get('pdf')
    
        
        if not customer_id:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not amount:
            return Response({"error": "amount not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not pdf :
            return Response({"error": "pdf not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        payment = Statement.objects.create(user_id=customer_id,amount=amount,pdf=pdf)
        
        return Response({"message": "Success Payment"}, status=status.HTTP_200_OK)
    
    
    def put(self,request):
        customer_id = request.data.get('user_id')
        
        if not customer_id:
            return Response({"error": "customer_token not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = Statement.objects.filter(user_id=customer_id).all()
        list_payment = []
        print(payment)
        for item in payment:
            payment_json = {"id": item.id, "user_id": item.user_id, "amount": item.amount, "pdf": item.pdf,"status": item.status,"code": item.code}
            list_payment.append(payment_json)
            
            
        
        return Response({"payment":list_payment }, status=status.HTTP_200_OK)
        
    

    def get(self,request):
        payments = Statement.objects.all()
        payment_list = []
        
        
        for payment in payments:
            print(payment)
          
            
            payment_json = {"id": payment.id, "amount": payment.amount, "pdf": payment.pdf,"status": payment.status,"code": payment.code}
            payment_list.append(payment_json)
        return Response({"payments": payment_list}, status=status.HTTP_200_OK)
        
    
    def delete(self,request):
        payment_id = request.data.get('payment_id')
        
        if not payment_id:
            return Response({"error": "payment_id not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = Statement.objects.get(id=payment_id)
        payment.delete()
        
        
        return Response({"message": "Delete Payment Success"}, status=status.HTTP_200_OK)
    

class PaymentInvoiceManage(APIView):
    
    def put(self,request):
        payment_id = request.data.get('payment_id')
        statustemp = request.data.get('status')
        
        if not payment_id:
            return Response({"error": "payment_id not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not status:
            return Response({"error": "status not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = Statement.objects.get(id=payment_id)
        payment.status = statustemp
        payment.save()
        
        
        return Response({"message": "Update Payment Success"}, status=status.HTTP_200_OK)

    def post(self,request):
        payment_id = request.data.get('payment_id')
        code = request.data.get('code')
        
        if not payment_id:
            return Response({"error": "payment_id not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not code:
            return Response({"error": "code not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = Statement.objects.get(id=payment_id)
        payment.code = code
        payment.save()
        
        return Response({"message": "Update Payment Success"}, status=status.HTTP_200_OK)
    
    
    
    
        
        
        
        
        
        
        
        

        
    

