# Exception
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError :
    file = open("a_file.txt",'w')
except KeyError as err_msg :
    print(f"The key {err_msg} was not found")  
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed successfully")