#!/usr/bin/python

# teaching loops to grade 4 students!

# PRINT 0 TO 4
count = 0;
while count < 5:
    print count
    count += 1

print "\n"

# PRINT 1 TO 10
count = 1
while count <= 10:
    print count
    count += 1
print "\n"

# DESCENDING 100 to 1

count = 100
while count >= 1:
    print count
    count -= 1

print "\n"

# PRINT MADDIE IS SUPER COOL
count = 1
while count <= 10:
    print "MADDIE IS SUPER COOL!"
    count += 1


print "\n"

# PRINT 0 TO 9
for i in range (10):
    print i
print "\n"

# PRINT 0, 1, 2
for i in range(0, 3):
    print "i = %d" % (i)
print "\n"
 
# DESCENDING FROM 100 TO 1
for i in range(10, 0, -1):
    print i
print "\n"

# EVERY OTHER FROM 3 TO 8
for i in range(1, 10, 1):
    print "This is iteration #", i

print "\n"

# COMPUTER LETTERS
word = "computer"
for letter in word:
    print letter
print "\n"

# PRINT FROM 5 to 50
for i in range(5, 51):
    print i
print "\n"

# HOTDOG LETTERS
for letter in "DUMPLINGS":
    print letter
print "\n"

# MULTIPLIED BY TWO
for i in range(1, 10, 1):
    print i*2
print "\n"

# EVEN NUMBERS
for i in range(50, 101, 2):
    print i


