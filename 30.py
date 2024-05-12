#class to implement pow(x, n)

class Pow:
    def __init__(self):
        pass

    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x * self.pow(x, n-1)