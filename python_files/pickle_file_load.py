import pickle

with open("python_files\save_file.pkl", "rb") as file:
    values = pickle.load(file)
    
print(values)