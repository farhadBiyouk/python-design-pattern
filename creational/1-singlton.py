"""
    Caretional : Singleton
           usage : just one object from class
            implementation   5 method  => 3 method  => class base
            __init__, __new__, __call__
"""


#  method 1
class Database:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


d1 =  Database()
d2=  Database()


print(id(d1))
print(id(d2))

# example2
class SSHHandlerConnection:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


ssh1 = SSHHandlerConnection()
ssh2 = SSHHandlerConnection()

print(id(ssh1))
print(id(ssh2))


# method 2


class Singleton(type):
    instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super(Singleton, self).__call__()
        return self.instance


class Database(metaclass=Singleton):
    pass


d1 = Database()
d2 = Database()

print(id(d1))
print(id(d2))
