#start_chat function definition.
def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu :
        menu_choices ="what do you want to do ? \n 1. Add a status update \n 2. Close application"
        result = int(raw_input(menu_choices))

        #valadating users input
        if (result == 1):
            #action 1
            pass
        elif (result==2):
            show_menu =False
        else:
            print "Wrong choice ,Try again."