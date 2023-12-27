# import turtle
#
# import test
#
# print(test.test_variable)
#
# peterson = turtle.Turtle()
#
# peterson.shape("turtle")
#
#
# peterson.setx(50)
#
# peterson.left(90)
# peterson.sety(100)
#
#
#
# peterson.color("coral")
#
# #or we can write the above code as follows:
# # from turtle import Turtle
# # peterson = Turtle()
#
# print(peterson)
#
# my_screen = turtle.Screen()
#
#
# my_screen.exitonclick()

import prettytable

my_table = prettytable.PrettyTable()

print(my_table.align)
my_table.add_column("Top Terrorist", [1,2,3,4,5])
my_table.add_column("Names", ["USA","Israel","France","UK","China"])
print(my_table.align)

my_table.align="l"
print(my_table)


