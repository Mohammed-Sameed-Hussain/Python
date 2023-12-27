with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode='w') as file:
    file.write("New content here")
    # this 'w' mode will only allow to overwrite the file (even the previous data gets deleted/ overwritten by the
    # new data) when we try to open a file in write mode, and if it does not exist then a new file with the given name
    # will be generated
with open("my_file.txt", mode='a') as file:
    file.write("\nNew content here")

with open("D:\OneDrive - IIT Hyderabad\Desktop\my_new_file.txt", mode='a') as file:
    file.write("New content here")
