import abc

class ModelInterface(abc.ABC) :
    @abc.abstractmethod
    def create( **data) :
        pass
    
    @abc.abstractmethod
    def update( data) :
        pass
    
    @abc.abstractmethod
    def delete( data) :
        pass
    @abc.abstractmethod
    def get( data) :
        pass
    
    @abc.abstractmethod
    def filter( data) :
        pass
    
    @abc.abstractmethod
    def all() :
        pass
    
    @abc.abstractmethod
    def get_or_create( data) :
        pass