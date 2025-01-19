"""
Cretional : Builder
have important class as Director which your task is  return ultimate product/
product is Car
"""
from abc import ABC, abstractmethod


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_info(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        return car


#  setter
class Car:
    def __init__(self):
        self.__wheel = None
        self.__body = None
        self.__engine = None

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine

    def detail(self):
        print(f'Body:  {self.__body.shape} -  Wheel:  {self.__wheel.size} -  Engine:  {self.__engine.hp}')


#  getter
class Builder(ABC):
    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass


class Bmw(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'Coupe'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine


class Maserati(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine


# ------------------------------------Component
class Wheel: size = None


class Body: shape = None


class Engine: hp = None


maz = Maserati()
director = Director()
director.set_builder(maz)
b1 = director.get_info()
b1.detail()
