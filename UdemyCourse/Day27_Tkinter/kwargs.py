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
