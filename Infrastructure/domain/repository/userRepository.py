from Infrastructure.domain.interface.model import ModelInterface
from payment.models import User

class userRepository(ModelInterface):
    
    
        
    def create(data):
        return User.objects.create(**data)
    
    def update( data):
       pass
    
    def delete( data):
        pass
    
    def get( data):
        pass
    
    def filter( data):
        pass
    
    def all():
        pass
    
    def get_or_create( data):
        pass
    