#1-m
class Student:
    def __init__(self,fullname, grade):
        self.fullname = fullname 
        self._grade = grade
        
    def get_grade(self):
        return self._grade
    
    def set_grade(self,new_grade):
        self.new_grade = new_grade 
        
             if self.new_grade == 1 or self.new_grade == 5:
                 return "Baho yangilansin"
             
             
             
s1 = Student("ali", 5)
print(s1.get_grade())

rse = s1.get_grade()
print(rse)

s1.get_grade()
print(s1.get_grade())
