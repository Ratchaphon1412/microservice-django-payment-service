from ..interface.topicInterface import TopicInterface
from Infrastructure.domain.repository.userRepository import userRepository
from Infrastructure.service import Facade

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
        message_decode = message.decode('utf-8')
        data = {
            "user_id":message_decode
            
        }
        header={
            "Content-Type":"application/json"
        }
        
        try:
            response = Facade.apiService().post('http://192.168.1.105:8024/api/v1/user/infrastructures/',data,header)
            response_json = response.json()
    
            customer_omise_id = Facade.omiseService().createCustomer(response_json['user']['email'],response_json['user']['fullname'])
            
            data = {
                "id":response_json['user']['id'],
                "email":response_json['user']['email'],
                "description":response_json['user']['fullname'],
                "phone":response_json['user']['phone'],
                "customer_omise_id":customer_omise_id,
            }
            
            
            
            userRepository.create(data)
            

            
        except Exception as e:
            print(e)

class TopicUserUpdate(TopicInterface):
    def action( message):
        print("User Update")