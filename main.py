print "Let's get started"
spy_name = raw_input("Provide your name here :")
if len(spy_name) > 0:
    print 'welcome ' + spy_name + " glad to have you"
    if len(spy_name)>0:
        spy_salutation = raw_input("what should we call you?")
        if len(spy_salutation)>0:
        # concatination of salutation and name.
            spy_name = spy_salutation + " " + spy_name
            print "Welcome "+ spy_name + '\nWe are glad to have you back'
        else:
             print "You did not entered your salutation.Please retry!"

else:
     print "You did not entered your name. Please retry!"