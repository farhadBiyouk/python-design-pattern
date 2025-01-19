"""
    Creational: Prototype
        refer to shallow and deep copy
"""
from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    def __init__(self):
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloneObj = deepcopy(self._object.get(name))
        cloneObj.__dict__.update(kwargs)
        return cloneObj



p1 = Person('amir', 34)
proto = Prototype()
proto.register('p2', p1)
person_clone = proto.clone('p2', age=24)
print(person_clone.__dict__)