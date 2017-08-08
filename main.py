print "Let's get started"
spy_name = raw_input("Provide your name here :")
if len(spy_name)>0:

    spy_salutation = raw_input("what should we call you?")
    if len(spy_salutation) > 0:
        # concatination of salutation and name.
        spy_name = spy_salutation + " " + spy_name
        print "Welcome " + spy_name + '\nWe are glad to have you back'
        print "Alright " + spy_name + ", I would like to know a little bit more about you before proceeding further."
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_age = int(raw_input("What is your age?"))
        print type(spy_age)
        if spy_age>12 and spy_age<50:
            print "Can you please tell us your spy rating: "
            spy_rating = float(raw_input("Enter your rating: "))
            if spy_rating > 4.7:
                print "Great Work Spy!"
            elif spy_rating > 3.5 and spy_rating <= 4.7:
                print "You are doing amazing Spy!"
            elif spy_rating > 2 and spy_rating <= 3.5:
                print "Can do much better Spy!"
            else:
                print "You need to buckle up Spy!"
            spy_online = True;
            print type(spy_online);
            print "Authentication complete. Welcome " + spy_name + "\n" + "age: ", spy_age, "\nRating: ", spy_rating, "\nOnline: ", spy_online
        else:
            print "Sorry, you are not eligible to be a spy."

    else:
         print "You did not entered your salutation.Please retry!"

else:
     print "You did not entered your name. Please try again !"