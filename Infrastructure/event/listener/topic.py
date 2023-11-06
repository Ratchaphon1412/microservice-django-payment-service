from ..interface.topicInterface import TopicInterface
from Infrastructure.domain.repository.userRepository import userRepository
from Infrastructure.service import Facade
from Infrastructure.kafka.producer import sendData
import json

from payment.models import User

class Listener:
    def run(topic,message):
        
        if topic == "create_user":
            TopicUserCreate.action(message)
        elif topic == "user_update":
            TopicUserUpdate.action(message)
        else:
            pass


class TopicUserCreate(TopicInterface):
    def action( message):
        print(message)
        message_decode = message.decode('utf-8')
        
        data = json.loads(message_decode)
        print(data)
        payment_service = Facade.omiseService()
        customer = payment_service.createCustomer(data['email'],data['username'])
        print('customer')
        
        
        
        try:
            
            user = User.objects.create(id=data['id'],email=data['email'],username=data['username'],customer_omise_id=customer)
            temp ={
                "id":data['id'],
                "customer_omise_id":user.customer_omise_id
            }
            print('send data')
            
            sendData("payment_customer",json.dumps(temp))
        except Exception as e:
            print(e)
            
            
    
    
        
        
     
        
        
        
        
        
        
        
      
        
        
class TopicUserUpdate(TopicInterface):
    def action( message):
        print("User Update")