def add(*args):
    print(args)
    print(type(args))
    total = 0
    for number in args:
        total = total + number
    return total


print(add(1, 2, 3, 4, 5))
