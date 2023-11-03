from .factory.renderpdf import RenderPDF
from .factory.paymentFactory.omisePayment import OmisePayment
from .factory.api import APICall

class Facade:

    global renderObject 
    global omisePayment
    renderObject = RenderPDF()
    omisePayment = OmisePayment()
    
      
         
  
    
    
    def renderService(template_src, data):
        
        return renderObject.render(template_src, data)
    
    def omiseService():
        return omisePayment

    def apiService():
        return APICall

    
