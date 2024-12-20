# stock.py
#
# Exercise 4.1


class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value

    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"
