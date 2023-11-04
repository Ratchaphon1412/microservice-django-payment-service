from .factory.renderpdf import RenderPDF
from .factory.paymentFactory.omisePayment import OmisePayment
from .factory.paymentFactory.promptpay import PromptPay
from .factory.api import APICall



class Facade:

    global renderObject 
    global omisePayment
    global promptpay
    renderObject = RenderPDF()
    omisePayment = OmisePayment()
    promptpay = PromptPay()
    
    
    
      
         
  
    
    
    def renderService(template_src, data):
        
        return renderObject.render(template_src, data)
    
    def omiseService():
        return omisePayment

    def apiService():
        return APICall

    def promptpayService():
        return promptpay
    
