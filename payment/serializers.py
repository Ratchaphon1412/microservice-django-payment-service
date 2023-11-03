from rest_framework import serializers
from payment.models import User

class CustomerPaymentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    description = serializers.CharField()

    def validate_email(self, value):
        # Check if email exists in User model
        if User.objects.filter(email=value).exists() == False:
            raise serializers.ValidationError("Email not found")
        
        return value

    def validate_description(self, value):
        # Add custom description validation logic here
        if value == False:
            raise serializers.ValidationError("Description not found")
        
        return value
    
class CardCustomerPaymentSerializer(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.CharField()
    expiration_month = serializers.CharField()
    expiration_year = serializers.CharField()
    city = serializers.CharField()
    postal_code = serializers.CharField()
    security_code = serializers.CharField()
    
    def validate(self, data):
        # Add custom validation logic here
        if len(data['name']) == 0:
            raise serializers.ValidationError("Name not found")
        if len(data['number']) != 16:
            raise serializers.ValidationError("Invalid card number")
        if len(data['expiration_month']) != 2:
            raise serializers.ValidationError("Invalid expiration month")
        if len(data['expiration_year']) != 4:
            raise serializers.ValidationError("Invalid expiration year")
        if len(data['city']) == 0:
            raise serializers.ValidationError("City not found")
        if len(data['postal_code']) == 0:
            raise serializers.ValidationError("Postal code not found")
        if len(data['security_code']) != 3:
            raise serializers.ValidationError("Invalid security code")

        return data