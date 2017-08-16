def add_status():

    # logic
    STATUS_MESSAGES = ["Spy mode ON", "No message, only call"]
    default = raw_input("Do you want to select from older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message)>0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        else:
            # logic
            print "Please enter a valid status "

    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) +". "+ str(message)
            item_position = item_position + 1
        message_selection = int(raw_input("Choose from the previous status: "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
        else:
            # logic
            print "Select a proper status"

    else:
        print "Wrong choice. Please try again"

    return updated_status_message