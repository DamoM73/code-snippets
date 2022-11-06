import csv


with open("netflix_titles.csv", encoding="utf-8") as netflix_file:

    csv_reader = csv.reader(netflix_file, delimiter=",")
    
    #print(csv_reader)
    
    
    for row in csv_reader:
        print(row[4].split(", "))
        
    """ print(next(csv_reader))
    print(next(csv_reader)) """    