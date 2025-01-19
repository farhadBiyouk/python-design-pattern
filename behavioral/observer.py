class Observer:

    def __init__(self):
        self._observers = []

    def attach_observer(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):
    def __init__(self, name):
        super(Data, self).__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class One:
    def update(self, subject):
        print(f'from one . {subject.name} modified. the new data is {subject.data}')


data = Data('First')
data.attach_observer(One())
data.data = 45