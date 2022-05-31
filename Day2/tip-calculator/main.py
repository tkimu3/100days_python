#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? ") )

# When converting to the particular format, which is the two decimal places,
# Not all numbers can be represented exactry by using round function since the computers
# stores floating point numbers as an integer and then divid it by a power of two.
# (ex) 13.95 will be represented in a similar fashion to 125650429603636838/(2**53).

# "Limiting floats to two decimal points"
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

# "How to round to 2 decimals with Python?"
# https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

# tip_included = round((total / num_people) * (100 + tip_percent) / 100,2)
tip_included = (total / num_people) * (100 + tip_percent) / 100

# Use Stfing format method to create the string
tip_rounded = "{:.2f}".format(tip_included, 2)

print (f"Each person should pay: ${tip_rounded}")