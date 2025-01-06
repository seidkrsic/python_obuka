


# objektno-orjentisano programiranje 

class Student: 
    def __init__(self, name, house, age): 
        if house not in ["Gryffindor", "Slytherin"]:
            raise ValueError("Invalid house")

        if age < 0: 
            raise ValueError("Age must me positive.") 
        self._name = name 
        self.house = house 
        self.age = age 

    # @getter 
    @property
    def name(self): 
        return self._name 
    
    @name.setter 
    def name(self, name): 
        if not name: 
            raise ValueError("Missing name.") 
        self._name = name 

    def __str__(self):
        return f"{self.name} from {self.house}" 
    
    def is_man(self): 
        if self.age >=18: 
            print(f"{self.name} is man.") 
        else: 
            print(f"{self.name} is a kid.")


def main(): 
    student = get_student() 
    print(student.name) 
    print(student.name)    


def get_student(): 
    name = input("Name: ") 
    house = input("House: ") 
    age = int(input("Age: "))
     # Student("Harry", "Gryffindor")
    return Student(name, house, age)


if __name__ == "__main__": 
    main() 