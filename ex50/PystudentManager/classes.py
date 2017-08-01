students = []

class Student:
    
    school_name = "Springfield Elementary"
#sets the student name and student id to the argument
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)
#Returns the student as a string
    def __str__(self):
       return "Student " + self.name
    
#capitalize the name of the student.
        
    def get_name_capitalize(self):
       return self.name.capitalize()
       
    def get_school_name(self):
        return self.school_name
        
        
class HighSchoolStudent(Student):
    
    school_name = "Springfield High School"
    
    def get_school_name(self):
        return "This is a High School student"
        
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
    
james = HighSchoolStudent("james")
print(james.get_name_capitalize())