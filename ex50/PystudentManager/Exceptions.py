student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None

}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    number_last_name = 3 + last_name
except KeyError:
    print("Error finiding last_name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)
    
print("This code executes!")
