student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None

}

#Prints out only the name of the student
print student['name']

#Throws an error due to the unknown value last_name
#student["last_name"]
#This will return KeyError

#Will tell you if the last value is unknow without throwing an error.
print student.get("last_name", "Unknown")

#Shows what keys or variable are listed
print student.keys()

#Gives all the values set to the variables in order of appreance.
print student.values()

#Will delete a given value
#del student["name"]