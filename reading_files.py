file = open("names.txt","r")

names = file.readlines()


for index, name in enumerate(names):
    print(f"{index} {name.strip()}")