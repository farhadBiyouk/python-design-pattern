'''
    Abstract factory
    CAR => Benz, BMW => SUV , Coupe
    benz suv => gla, glc
    bmw suv => x1 , x2

    benz coupe => cls E-class
    bmw  coupe => m2 , m4
'''
from abc import ABC, abstractmethod


# -----------------------------------------------creator

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


class Benz(Car):
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()


class Bmw(Car):
    def call_suv(self):
        return X1()

    def call_coupe(self):
        return M2()


# -----------------------------------------------


# ------------------------------------------------product

class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass


class Gla(Suv):
    def create_suv(self):
        print('your gla from benz and model is suv')


class X1(Suv):
    def create_suv(self):
        print('your x1 from bmw and model is suv')


class Cls(Coupe):
    def create_coupe(self):
        print('your cls from benz and model is coupe')


class M2(Coupe):
    def create_coupe(self):
        print('your m2 from bmw and model is coupe')


# ---------------------------------------------------------


# ----------------------------------------------------------

def client_suv(format):
    result = format.call_suv()
    result.create_suv()


def client_coupe(format):
    result = format.call_coupe()
    result.create_coupe()
# ----------------------------------------------------------



client_suv(Benz())
client_suv(Bmw())
client_coupe(Benz())
client_coupe(Bmw())
