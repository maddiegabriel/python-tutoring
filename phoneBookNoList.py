#!/usr/bin/python

# phone book without list - to demo why we need data structures
# will adapt with list later

while True:
    print "Would you like to enter a new contact?"
    answer = raw_input()

    if answer == "No":
        break
    else:
        while True:
            print "What is your name?"
            name = raw_input()
            if name.isalpha() == True:
                break

        while True:
            print "What is your phone number?"
            number = raw_input()
            if ((number.isalpha() == False) and (len(number) == 10)):
                break;

        print "Thank you %s! Your phone number is %s" % (name, number)


