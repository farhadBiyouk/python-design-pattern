from abc import ABC, abstractmethod


class Top(ABC):

    def tamplate_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()
        self.hook()

    def first_common(self):
        print('I am first common')

    def second_common(self):
        print('I am second common')

    @abstractmethod
    def third_require(self):
        pass

    @abstractmethod
    def fourth_require(self):
        pass

    def hook(self):
        pass


class One(Top):

    def third_require(self):
        print('i am third require from one')

    def fourth_require(self):
        print('i a fourth require from one')

    def hook(self):
        print('i am hook from one')


class Two(Top):

    def third_require(self):
        print('i am third require from Two')

    def fourth_require(self):
        print('i a fourth require from two')


def client(class_):
    class_.tamplate_method()


client(One())