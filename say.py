#!/usr/bin/python

# fun with say function

# import these so we can use say and randint
from os import system

# the say function uses built in OSX "say" command to convert text to speech
def say(something):
    system('say "%s"' % something)

say("Now listen closely Heres a little lesson in trickery This is going down in history If you wanna be a Villain Number One You have to chase a superhero on the run Just follow my moves, and sneak around Be careful not to make a soundShhC R U N C H")

say("No, dont touch that! We are Number One Hey! We are Number One Ha ha ha Now look at this net, that I just found When I say go, be ready to throw Go!Throw it at him, not me! Ugh, lets try something else")
say("Now watch and learn, heres the deal He'll slip and slide on this banana peel Ha ha ha, WHAT ARE YOU DOING!? ba-ba-biddly-ba-ba-ba-ba, ba-ba-ba-ba-ba-ba-ba We are Number One Hey!")
say("ba-ba-biddly-ba-ba-ba-ba, ba-ba-ba-ba-ba-ba-ba We are Number One ba-ba-biddly-ba-ba-ba-ba, ba-ba-ba-ba-ba-ba-ba We are Number One Hey! ba-ba-biddly-ba-ba-ba-ba, ba-ba-ba-ba-ba-ba-ba We are Number One Hey! Hey!.")