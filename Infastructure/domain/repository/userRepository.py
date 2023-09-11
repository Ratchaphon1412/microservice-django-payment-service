from domain.interface.model import ModelInterface


class userRepository(ModelInterface):
    
    def __init__(self, user):
        self.user = user
        
    def create(self, data):
        return self.user.objects.create(**data)
    
    def update(self, data):
        return self.user.objects.update(**data)
    
    def delete(self, data):
        return self.user.objects.delete(**data)
    
    def get(self, data):
        return self.user.objects.get(**data)
    
    def filter(self, data):
        return self.user.objects.filter(**data)
    
    def all(self):
        return self.user.objects.all()
    
    def get_or_create(self, data):
        return self.user.objects.get_or_create(**data)
    