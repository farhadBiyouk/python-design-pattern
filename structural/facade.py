"""
Structural: Facade
"""
class Raw:
    def raw(self):
        print('Buying raw foods from market')


class Transfer:
    def transfer(self):
        print('Transferring raw foods to kitchen')


class Cook:
    def cook(self):
        print('cooking foods by chief')


class Serve:
    def serve(self):
        print('serving foods')


class ItalianRestaurant:   # facade
    def get(self):
        r = Raw()
        r.raw()

        t = Transfer()
        t.transfer()

        c = Cook()
        c.cook()

        s = Serve()
        s.serve()


def order():
    i =  ItalianRestaurant()
    i.get()


order()