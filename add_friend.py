# import statements.
from globals import friends,spy
from spy_details import Spy
import re
from colorama import init,Fore

init()

name_pattern = "^[a-zA-Z]+[\sa-zA-Z]*$"
age_pattern = "^[0-9]+$"
rating_pattern = "^[0-9]+\.[0-9]+$"

# add new friends.
def add_friend():
    new_friend = Spy(""," ",0,0.0)
    while True:
        new_name = raw_input("Please add your friend's name : ")
        if re.match(name_pattern, new_name) != None:
            break
        else:
            print(Fore.RED + "Name can have only alphabets & cannot be null neither name cannot start with space. Please provide a valid name." + Fore.RESET);
    if len(new_name) <= 0:
         print Fore.RED+ "Name is not entered"
    new_salutation = raw_input("How do you want to address your friend (Mr/Ms.) : ")
    new_friend.name = new_salutation + "." + new_name
    while True:
        new_age = raw_input("Please enter the age : ")
        if re.match(age_pattern , new_age) != None:
            new_friend.age = int(new_age)
            break
        else:
            print Fore.RED + "Age can only be integer. Please re enter age:"

    if new_friend.age <= 12 or new_friend.age >= 50:
        print Fore.RED+ "Age not supported"

    while True:
        new_rating = raw_input("Enter your friends rating:")
        if re.match(rating_pattern, new_rating) != None:
            new_friend.rating = float(new_rating)
            break
        else:
            print(Fore.RED + "Please provide a rating in decimal format. like 4.0 or 4.4 etc..!" + Fore.RESET)

    if new_friend.rating <= 5.0 and new_friend.age > 12 and new_friend.age < 50 :
        # add_friend
        friends.append(new_friend)
        print Fore.GREEN+"Friend is Added successfully"
    else:
        print Fore.RED+"Sorry invalid entry. We can not add your friend due to some error. Please check your details again."

    # returning number of friends
    return len(friends)
