#!/usr/bin/python

# import these so we can use say and randint
from os import system
from random import randint

# the say function uses built in OSX "say" command to convert text to speech
def say(something):
    system('say "%s"' % something)

say("Please enter your name:")
print("Please enter your name:")
name = raw_input()

# ask user for number between 1 and max number (your choice)
max_number = 10
print("Let's play a guessing game! Try to guess the number I'm thinking of.")
say("Let's play a guessing game! Try to guess the number I'm thinking of.")
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
        say("The number is lower")
    elif answer < number:
        say("The number is higher")
    #if they guessed correct, exit loop by setting solved = True!
    else:
        say("You got it right! Congratulations %s!" % name)
        print("You got it right! Congratulations %s!" % name)
        solved = True