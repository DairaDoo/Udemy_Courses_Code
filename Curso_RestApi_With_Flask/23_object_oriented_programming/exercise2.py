class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
        
student1 = Student("Bob", (100, 100, 93, 78, 90))
print("name: " , student1.name)
print("grades: ", student1.grades)

# one way is passing the object to the class the other simply calling the method in the same object.
print(Student.average_grade(student1))

# this is the best way of doing it. 
print(student1.average_grade())

print("\nOther Object")
student2 = Student("Dairan", (100, 100, 100, 100 , 100))
print(student2.average_grade())
    