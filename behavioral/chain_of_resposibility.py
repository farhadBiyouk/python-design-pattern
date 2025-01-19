"""
Behavioral:
    Chain of responsibility
"""
from abc import ABC, abstractmethod


class AbstractHAndler(ABC):

    def __init__(self, successor):
        self._successor = successor

    def handel(self, request):
        handler = self.processRequest(request)
        if not handler:
            self._successor.handel(request)

    @abstractmethod
    def processRequest(self, request):
        pass


class HandlerOne(AbstractHAndler):
    def processRequest(self, request):
        if 1 < request <= 10:
            print('this request processing with handler one : ', request)
            return True


class HandlerTwo(AbstractHAndler):
    def processRequest(self, request):
        if 10 < request <= 20:
            print('this request processing with handler two : ', request)
            return True


class DefaultHandler(AbstractHAndler):
    def processRequest(self, request):
        print('this request processing whit default handler: ', request)
        return True


class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, request):
        for req in request:
            self.handler.handel(req)


requests = [2, 14, 3, 16, 25]
c1 = Client()
c1.delegate(requests)
