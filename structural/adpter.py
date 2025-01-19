"""
Structural : Adapter
have 3 section => 1-adaptee, 2- adapter, 3- client
"""


class IranSocket:
    _type ='2'
class Adapter:
    _socket = None
    _pinType = '3To2'

    def __init__(self, socket):
        self._socket = socket
class Fridge:
    _adapter = None
    _pinType = '3'

    def __init__(self, adapter):
        self._adapter =adapter


    def freeze(self):
        if self._adapter._pinType ==(self._pinType +'To'+ self._adapter._socket._type):
            print("Done")
        else:
            print('Noooooooooooooooooo')


ir = IranSocket()
adapter = Adapter(ir)
fridge = Fridge(adapter)
fridge.freeze()