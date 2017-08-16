# import statements.
from spy_details import spy
from start_chat import start_chat

print "Let's get started!!!"
question = "Do you want to continue as " + spy['salutation'] + spy['name'] + "(Y/N) ? "
existing = raw_input(question)

# validating users input
if existing.upper() == "Y":
    spy_name = spy['salutation'] + " " + spy['name']
    # default user
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])

elif existing.upper() == "N":
    # new user code here
    spy['name'] = raw_input("What is your name SPY: ")  # defining variable.

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("What should we call you(Mr. or Ms.): ")
        spy['age'] = int(raw_input("Please enter your age : "))           # typecasting(converting string to int)

        spy['name'] = spy['salutation'] + "" + spy['name']  # concatenation of name and salutation
        # assignment operator parsing is from r to l.

        spy['rating'] = float(raw_input("What is your spy rating?"))  # typecasting(int to float)
        spy_is_online = True

        # starting chat application
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])

    else:
        print "Invalid name. Please try again."
else:
    print "Wrong choice. Try again"