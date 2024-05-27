from typing import List, Optional

# it is recommended to not use default parameter values
class Student:
    def __init__(self, name: str, grades: List[int] = []): # this is bad!
        self.name = name
        self.grades = grades
        
    def take_exam(self, result: int):
        self.grades.append(result)
        
# Better solution
class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): # this is better!
        self.name = name
        self.grades = grades or []
        
    def take_exam(self, result: int):
        self.grades.append(result)
        

dairan = Student("dairan")
ian = Student("ian")
dairan.take_exam(90)
print(dairan.grades)
print(ian.grades)