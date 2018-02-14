#!usr/bin/python

# simple python rock paper scissors game for kids to make

print "~~~~~~~~~~~ Welcome to Rock Paper Scissors! ~~~~~~~~~~~"

# get names from both players
user1 = raw_input("Player 1 - what's your name? ")
user2 = raw_input("Player 2 - what's your name? ")

# this loop will never stop until we break out of it from the inside!
while True:
    # get both users' choices (rock/paper/scissors)
    u1_answer = raw_input("%s, do you choose rock, paper or scissors? " % user1)
    u2_answer = raw_input("%s, do you choose rock, paper or scissors? " % user2)
    
    if u1_answer == u2_answer:
        # both users chose the same - it's a tie!
        print "It's a tie!"
    elif u1_answer == 'rock':
        # if user 1 chose rock and
        # user 2 chose scissors: user 1 won
        # user 2 chose PAPER: user 2 won
            # question for you guys: why can we use "else" here and it means the same as "u2_answer == 'paper'"?
        if u2_answer == 'scissors':
            print "%s wins!" % user1
        else:
            print "%s wins!" % user2
    elif u1_answer == 'scissors':
        if u2_answer == 'paper':
            print "%s win!" % user1
        else:
            print "%s wins!" % user2
    elif u1_answer == 'paper':
        if u2_answer == 'rock':
            print "%s wins!" % user1
        else:
            print "%s wins!" % user2
    else:
        # if the user entered something OTHER than rock/paper/scissors
        print "Invalid input! You have not entered rock, paper or scissors, try again."
        break
    # after the round is over, ask if they want to play again! only break out of the loop if they answer "no"
    print "Want to play another round?"
    play = raw_input()
    if(play == 'no' or play == 'No'):
        break

