import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def charge(self, amount, token):
        pass