class Quadratic():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # def quad(self, x):
    #     return self._a * x**2 + self._b * x + self._c

    def __call__(self, x):
        return (self._a * x**2) + (self._b * x) + self._c
