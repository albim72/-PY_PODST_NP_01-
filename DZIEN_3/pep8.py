g: int

def testowa(a, b):
    global __g
    info = "ab"
    _t = "obliczenie nr 1"
    __g = 56
    return (a + b) * __g


print(testowa(4, 6))
print(__g)


class Test:
    def __init__(self, x):
        self.hx = None
        self.x = x

    __h = 10
    _hx = 9

    def liczmy(self):
        return self.__h + self.x

    # @property
    # def hx(self):
    #     return self._hx


t = Test(56)
print(t.liczmy())
print(t.hx)
# print(Test.__h)
