# try:
#     file = open("test.txt")
#     a_dictionary = { "key" : "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("test.txt", 'w')
#     file.write("Something")
# except KeyError as err_msg:
#     print(f"The key {err_msg}: That key does not exist!")
#
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error I conjured up")

height = float(input("Height: "))
weight = int(input("Weight:"))

if height > 3  :
    raise ValueError("The height is not Human! hehe")

bmi = weight / height **2
print(bmi)