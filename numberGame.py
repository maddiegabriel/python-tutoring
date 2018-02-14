#!/usr/bin/python

# import these so we can use say and randint
from os import system
from random import randint

# the say function uses built in OSX "say" command to convert text to speech
def say(something):
    system('say "%s"' % something)

print("Please enter your name:")
say("Please enter your name:")
name = raw_input()

# ask user for number between 1 and max number (your choice)
max_number = 10
print("Hi %s! Let's play a guessing game!\nTry to guess the number I'm thinking of." % name)
say("Hi %s! Let's play a guessing game!\nTry to guess the number I'm thinking of." % name)
print("Pick a number between 1 and %d" % max_number)
say("Pick a number between 1 and %d" % max_number)

# pick a random number between 1 and max number as the answer
number = randint(1, max_number)

# solved is false: the puzzle has not yet been solved
solved = False

#keep looping unil we guess correctly (aka until solved = True)
while (solved == False):
    #set user input to answer
    answer = input()
    #check if the user's input is lower/higher than the real number
    if answer > number:
        print("The number is lower - try again!")
        say("The number is lower - try again!")
    elif answer < number:
        print("The number is higher - try again!")
        say("The number is higher - try again!")
    #if they guessed correct, exit loop by setting solved = True!
    else:
        print("You got it right! Congratulations %s!" % name)
        say("You got it right! Congratulations %s!" % name)
        solved = True