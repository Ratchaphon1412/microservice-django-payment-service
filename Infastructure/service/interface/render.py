import abc

class Render(abc.ABC) :
    @abc.abstractmethod
    def render(self,template_src, data) :
        pass
    