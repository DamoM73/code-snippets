value = "String that will be written to text file"

with open("python_files\save_variable.txt", "w") as file:
    file.write(value)
