# import statements.
from globals import friends

# add new friends.
def add_friend():
    new_friend = {
        'name': '',
        'salutation': '.',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
        'chats' : []
    }

    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    # concatenation
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = int(raw_input("Age?"))
    new_friend['rating'] = float(raw_input("Spy rating?"))

    # validating input
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 60:
        # add_friend
        friends.append(new_friend)
        print "Friend Added"
    else:
        print "Sorry invalid entry. We can not add your friend due to some error. Please check your details again."

    # returning number of friends
    return len(friends)