


d = {"A" : 1, "B" : 2} 


students = { 
    "Hermoine" : "Gryffindor", 
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Draco" : "Slytherin",
} 

# print(students["Harry"]) 
# print(students["Draco"]) 

# for student in students:  # "Hermoine"
#     print(student, students[student])  # students["Hermoine"]

# JSON --- > dictionary 
# students = [ 
#     {"name" : "Hermoine", "house" : "Gryffindor", "age" : 14 }, 
#     {"name" : "Harry", "house" : "Gryffindor", "age" : 13 }, 
#     {"name" : "Draco", "house" : "Slytherin", "age" : 15 },  
# ] 

# for student in students: 
#     print(f"{student['name']}, {student['house']}, {student['age']}")  


students = { 
    "Hermoine" : "Gryffindor", 
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Draco" : "Slytherin",
} 
    #                                       0 1
for key, value in students.items():   # tuple (1,2)
    print(key, value) 

del students["Draco"] 
print(students) 
students["Seid"] = 5 
print(students) 