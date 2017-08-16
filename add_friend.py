def add_friend():
    friends_name = []
    friends_age = []
    friends_rating = []
    friends_is_online = []

    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = int(raw_input("Age?"))
    new_rating = float(raw_input("Spy rating?"))

    if len(new_name)>0 and new_age>12 and new_age<60:
        # add_friend
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
    else:
        print "Sorry invalid entry. We can not add your friend due to some error. Please check your details again."

    return len(friends_name)
