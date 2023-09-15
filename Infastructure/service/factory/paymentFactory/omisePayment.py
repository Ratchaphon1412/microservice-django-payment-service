from django.conf import settings
import omise
class OmisePayment:
    def __init__(self):
        self.api_secrete = settings.OMISE_SECRETE
        omise.api_secret = self.api_secrete
        
        
    def adminBalance(self):
        
        balance = omise.Balance.retrieve()
        return balance.total