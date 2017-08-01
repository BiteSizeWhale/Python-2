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
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                                "(or 'y' or 'n').\n")

    