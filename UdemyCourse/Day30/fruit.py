fruits = eval(input())



def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit+'pie')
    except IndexError:
        print('fruit pie')
    else:
        print(fruit+'pie')