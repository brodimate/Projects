#!/usr/bin/env python3


class Sor:
    def __init__(self):
        self.data = []

    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def betesz(self, value):
        self.data.append(value)

    def kivesz(self):
        if len(self.data) != 0:
            return self.data.pop(0)
        else:
            return None

    def beszur(self, index, value):
        self.data.insert(index, value)

    def meret(self):
        return len(self.data)

    def __str__ (self):
        return "{s}".format(s=str(self.data))


def main():
   s = Sor()
   print(s)
   print(s.ures())
   s.betesz(1)
   s.betesz(3)
   s.betesz(6)
   s.beszur(2, 4)
   print(s)
   s.kivesz()
   print(s)
   print(s.meret())
   s.kivesz()
   s.kivesz()
   s.kivesz()
   x = s.kivesz()
   print(x)

if __name__ == "__main__":
    main()