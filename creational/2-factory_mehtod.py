'''
    Creatinal : Simple factory
        have 3 component=.> 1-creator 2- product 3- client
'''
from abc import ABC, abstractmethod


# -----------------------------------------creator

class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        edit = self.make()
        result = edit.edit()
        return result


class JsonCreator(Creator):
    def make(self):
        return JsonProduct()


class CSVCreator(Creator):
    def make(self):
        return CSVProduct()


# -----------------------------------------creator


# -----------------------------------------Product

class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class JsonProduct(Product):
    def edit(self):
        print('Editing with json ')


class CSVProduct(Product):
    def edit(self):
        print('Editing with csv file')
# -----------------------------------------


def client(format):
    format.call_edit()


client(CSVCreator())


