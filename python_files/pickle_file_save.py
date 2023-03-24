import pickle

values = ["Michelle", "Nicole", "Emma", "Justine", "Maria"]

with open("python_files/save_file.pkl", "wb") as file:
    pickle.dump(values, file)