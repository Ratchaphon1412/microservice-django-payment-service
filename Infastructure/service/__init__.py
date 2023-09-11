from .factory.renderpdf import RenderPDF

class Facade:

    global renderObject 
    renderObject = RenderPDF()
    
      
         
  
    
    
    def renderService(template_src, data):
        
        return renderObject.render(template_src, data)
    


    
