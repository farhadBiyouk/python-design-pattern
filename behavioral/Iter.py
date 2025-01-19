"""
    Iterator => 1- Iterable 2- Iteration
    __iter__, __next__
"""


class Iteration:
    def __init__(self, value):
        self._value = value

    def __next__(self):
        for i in range(0, self._value):
            value = self._value
            self._value -= 1
            return value

class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)



f1 = Iterable(9)
f2 = iter(f1)

print(next(f2))
print(next(f2))
