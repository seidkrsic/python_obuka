import csv 

import statistics 
students = [] 
# komentar 
with open("grades.csv", "r") as file:  # ovdje smo nesto radili... 
    file = csv.DictReader(file) 
    for line in file: 
        student = {} 
        student["name"] = line["Student"] 
        student["grade"] = round(statistics.mean([int(line["Math"]),int(line["Science"]),int(line["English"])]),2)
        students.append(student) 

with open("new_grades.csv", "w") as file: 
    new_file = csv.DictWriter(file, fieldnames=["name", "grades"]) 
    new_file.writeheader()
    for student in students:  
        new_file.writerow({"name" : student["name"], "grades" : student["grade"]}) 