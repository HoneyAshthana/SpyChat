# import statements.
from spy_details import Spy
from start_chat import start_chat
from globals import spy
from colorama import init,Fore
import re #for implementing regular expression
init()

name_pattern="^[a-zA-Z]+[\sa-zA-Z]*$"
age_pattern="^[0-9]+$"
rating_pattern="^[0-9]+\.[0-9]+$"

print "Let's get started!!!"
question = Fore.BLUE+"Do you want to continue as " + spy.salutation + spy.name + "(Y/N) ? "
existing = raw_input(question)

# validating users input
if existing.upper() == "Y":

    spy_name = spy.salutation + " " + spy.name
    # default user
    start_chat(spy.name,spy.age,spy.rating,spy.is_online)

elif existing.upper() == "N":
    # new user
    while True:
        spy.name = raw_input("What is your name SPY : ")  # defining variable.
        if re.match(name_pattern, spy.name) != None:
            break
        else:
            print( Fore.RED + "Name can only contain alphabets, name cannot be null and name cannot start with space. Please provide a valid name." + Fore.RESET);
    if len(spy.name) > 0:
        spy.salutation = raw_input("What should we call you(Mr. or Ms.): ")
    spy.name=spy.salutation + " " + spy.name
    print "Okay " + spy.name + "!! I would like to know more about you "
    while True:
        try:
            spy.age = int(raw_input("Please enter your age : "))
            # typecasting(converting string to int)
            if re.match(age_pattern, spy.age, flags=0) != None:
                spy.age=int(spy.age)
                break
            else:
                print(Fore.RED+"Age can only be a integer. Please re enter your age:"+Fore.RESET);
                break
        except ValueError:
            print Fore.RED+"Invalid age .Try again"


    while True:
        spy.rating = raw_input("Enter Spy rating : ")
        if re.match(rating_pattern, spy.rating) != None:
            spy.rating = float(spy.rating)
            break
        else:
            print Fore.RED+"Enter Again!!!!",
        # Checking If Spy is eligible
    if spy.rating <= 5.0 and spy.age > 12 and spy.age < 50:
        start_chat(spy.Name, spy.Age, spy.Rating, spy.SpyOnline)

    else:
        print Fore.RED+"Invalid Entry!!!!Start From Scratch."
else:
    print Fore.RED+"Wrong choice. Try again"
