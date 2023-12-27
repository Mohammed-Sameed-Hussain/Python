def add(*args):
    print(args)
    print(type(args))
    total = 0
    for number in args:
        total = total + number
    return total


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(2, add=54, multiply=56)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get('color')  # using kw.get does not throw error if the user does not pass the color argument!


my_car = Car(make="nissan", model="GT-R")
