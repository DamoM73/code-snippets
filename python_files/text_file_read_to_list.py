with open(r"python_files\names.txt", "r", encoding="utf-8") as file:
    data = file.read().split("\n")
    
print(data)