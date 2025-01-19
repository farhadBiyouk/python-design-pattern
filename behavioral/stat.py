class State:
    def operate(self):
        print(f'Turning tv {self.status}')


class TurnOn(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'On'


class TurnOff(State):
    def __init__(self, tv):
        self.tv = tv
        self.status = 'Off'


class Tv:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on

    def press(self):
        self.state.operate()
