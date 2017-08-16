from globals import friends

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend['name'] + "Age : " + str(friend['age'])
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
    return result - 1