students = []

#Gets user/students info
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase
#Makes the user infor be readable to the editor so the user can veiw it.
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)
#Adds the student to the list of other students
def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id }
    students.append(student)
    
def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save_file")
        
def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")
        
#Sets the student list to the info given in the get_stutdnets_titlecase method  
read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)