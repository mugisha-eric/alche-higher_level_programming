class Student:

    #class variable
    
    class_year = 2024
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name)
print(student2.age)
print(student1.class_year)
print(f"Total number of objects: {Student.count}")