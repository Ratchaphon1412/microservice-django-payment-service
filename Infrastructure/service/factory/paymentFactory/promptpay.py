from promptpay import qrcode
from django.conf import settings
import os
import time

class PromptPay:
    def __init__(self):
        self.phone = settings.PROMPTPAY_PHONE

    def qrcode(self, amount):
        payload = qrcode.generate_payload(self.phone, amount=amount)
        img = qrcode.to_image(payload)
        timestamp = int(time.time())
        filename = f"{self.phone}_{amount}_{timestamp}.png"
        
        filepath = os.path.join(settings.MEDIA_ROOT + '/qrcode/', filename)
        qrcode.to_file(payload, filepath) 
        
        return filename