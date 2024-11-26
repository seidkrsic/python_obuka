


# lists 
#               0          1       2 
students = ["Hermoine", "Harry", "Ron"]   
# print(students[0]) 
# print(students[1]) 
# print(students[2]) 

# laksi nacin prikaza elemenata liste 
# for student in students: 
#     print(student) 

# drugi nacin prikaza elemenata liste 
for i in range(len(students)): # [0,1,2]
    print(f"{i+1}. {students[i]}") 

# dodavanje elementa listi 
students.append("Seid") 

students[0] = 10 
print(students)   
del students[1] 
print(students) 
 
# list methods in python 
