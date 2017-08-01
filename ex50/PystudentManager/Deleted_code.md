#add_student("Mark", student_id=15)
#takes in all of the user info and assiens them.
#var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

#Adds all arguments to your program no matter how many a user puts in.
#$ Edit change args to kwargs which lets the terminal set varaiables to all of the inputs the user gives
#def var_args(name, **kwargs):
#    print(name)
#    print(kwargs["description"], kwargs["feedback"])




yes_no = []
 
def get_awnser():
    awnser_true = []
    for awnser in yes_no:
        awnser_true = awnser["awnser"].title()
    return awnser_true
def print_awnser():
    awnser_true = get_awnser()
    print(awnser_true)
    
    print_awnser()
    
    import sys

def query_yes_no(question, default="yes"):
    
    """Ask a yes/no question via raw_input() and return their answer.
    "question" is a string that is presenterd to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yest (the defult), "no" or None 
        (meaning an answer is required of the user).
    The "answer return balue is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
            "no": False, "n": False}
            
    if default is None:
        prompt = "[y/n]"
    elif default == "yes":
        prompt = " [y/n]"
    elif default == "no":
        prompt = "  [y/n] "
    else: 
        raise ValueError("invalid default answer: '%s'" %default)
    
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                                "(or 'y' or 'n').\n")
#mark = Student("Mark")
#print(mark)

print(Student.school_name)