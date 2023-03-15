values = ["Michelle", "Nicole", "Emma", "Justine", "Maria"]

with open("python_files\save_list.txt", "w") as file:
    for item in values:
        file.write(f"{item}\n")
