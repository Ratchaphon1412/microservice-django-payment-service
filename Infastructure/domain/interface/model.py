import abc

class ModelInterface(abc.ABC) :
    @abc.abstractmethod
    def create(self, data) :
        pass
    
    @abc.abstractmethod
    def update(self, data) :
        pass
    
    @abc.abstractmethod
    def delete(self, data) :
        pass
    @abc.abstractmethod
    def get(self, data) :
        pass
    
    @abc.abstractmethod
    def filter(self, data) :
        pass
    
    @abc.abstractmethod
    def all(self) :
        pass
    
    @abc.abstractmethod
    def get_or_create(self, data) :
        pass