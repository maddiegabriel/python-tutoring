#!/usr/bin/python

# very simple python cash register for a restaurant bill!
# concepts: user input, casting, branching, simple arithmetic, printing variables

print("Please enter the cost of your meal: ")
cost = float(raw_input())
if cost <= 0:
    print("Please enter a positive cost for your meal: ")
    cost = float(raw_input())

print("What percent would you like to tip?")
tip = float(raw_input())
if tip <= 0:
    print("Please enter a positive tip percent: ")
    tip = float(raw_input())

tip = float(tip/100)

#print("tip is: %f" % tip)

tax = 0.15

cost = cost + (cost * tax)
total_cost = cost + (cost * tip)

print("The total cost of your meal is: $%.2f" % total_cost)