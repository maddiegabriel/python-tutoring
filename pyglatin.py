#!/usr/bin/python

# program converts given word to PYG LATIN!!!
# example:
#   if the user enters the word "butter"
#   the program converts it to "utterbay"

pyg = 'ay'

# get word from user
original = raw_input('Enter a word: ')

# if the user entered a valid word
if len(original) > 0 and original.isalpha():
    #convert word to all lowercase
    word = original.lower()
    # grab the FIRST CHARACTER of the user's word
    first = word[0]
    # create a new word: butter + b + ay = "butterbay"
    new_word = word + first + pyg
    # get rid of first character of the new word: butterbay > "utterbay"
    new_word = new_word[1:len(new_word)]
    # print the new translated word!
    print original + " translated to pyg latin is: " + new_word
else:
    # if the user entered an invalid word, tell them and exit!
    print 'not a word, sorry!'