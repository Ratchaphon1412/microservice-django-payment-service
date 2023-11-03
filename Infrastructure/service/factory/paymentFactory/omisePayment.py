from django.conf import settings
import omise
class OmisePayment:
    def __init__(self):
        self.api_secrete = settings.OMISE_SECRETE
        self.api_public = settings.OMISE_PUBLIC
        omise.api_secret = self.api_secrete
        omise.api_public = self.api_public
        
        
    def adminBalance(self):
        
        balance = omise.Balance.retrieve()
        return balance.total
    
    def adminReceipt(self):
        receipts = omise.Receipt.retrieve()
        return receipts.data
    
    def adminReceiptDetail(self,receipt_id):
        receipt = omise.Receipt.retrieve(receipt_id)
        return receipt
    
    def createCustomer(self,email,description):
        customer = omise.Customer.create(
            email=email,
            description=description
        )
        return customer.id
    
    def deleteCustomer(self,customer_id):
        
        customer = omise.Customer.retrieve(customer_id)
        return customer.destroy()
    
    def getCustomer(self,customer_id):
        customer = omise.Customer.retrieve(customer_id)
        return customer
    
    def createCard(self,name,number,expiration_month,expiration_year,city,postal_code,security_code):
        token = omise.Token.create(
            name=name,
            number=number,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            city=city,
            postal_code=postal_code,
            security_code=security_code,
        )
        return token.id
    
    def addCardCustomer(self,customer_id,card_id):
        customer = omise.Customer.retrieve(customer_id)
        customer.update(card=card_id)
        return customer
    
    def deleteCustomerCard(self,customer_id,card_id):
        customer = omise.Customer.retrieve(customer_id)
        card = customer.cards.retrieve(card_id)
        
        return card.destroy()
    
    def listCustomerCard(self,customer_id):
        customer = omise.Customer.retrieve(customer_id)
        return customer.cards.data
    
    def paymentCardRegister(self,customer_id,card_id,amount,return_uri):
        charge = omise.Charge.create(
            amount=amount,
            currency="thb",
            customer=customer_id,
            card=card_id,
            return_uri=return_uri,
        )
        return charge
    
    def paymentCardOnetime(self,amount,token,return_uri):
        charge = omise.Charge.create(
            amount=amount,
            currency="thb",
            card=token,
            return_uri=return_uri,
        )
        
        return charge
    
    