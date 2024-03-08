import os
with open("check.txt", "a") as file:
    list = []
    print("Enter 'stop' to end.")
    while True:
        user_input = input("Please input data:")
        if (user_input == 'stop'):
            break
        list.append(user_input)
    for i in list:
        file.write(str(i))
        file.write('\n')
    file.close()
with open("check.txt",'r') as file:
    print(file.read())
    file.close()
os.remove("check.txt")
