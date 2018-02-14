#!/usr/bin/python

# !!!!!not kid friendly!!!!

# import these so we can use say and randint
from os import system
from random import randint

# the say function uses built in OSX "say" command to convert text to speech
def say(something):
    system('say "%s"' % something)

say("enter your name")
print("Please enter your name:")
name = raw_input()

# ask user for number between 1 and max number (your choice)
max_number = 10
print("Pick a number between 1 and %d" % max_number)
say("Pick a number between 1 and %d" % max_number)

# pick a random number between 1 and max number as the answer
number = randint(1, max_number)

# solved is false: the puzzle has not yet been solved
solved = False

#keep looping unil we guess correctly (until solved = True)
while (solved == False):
    #set user input to answer
    answer = input()
    #check if lower/higher
    if answer > number:
        say("The number is lower you dumb ass")
    elif answer < number:
        say("The number is higher you dumb ass")
    #if correct, exit loop
    else:
        say("You got it right! Congratulations ass hat!")
        solved = True