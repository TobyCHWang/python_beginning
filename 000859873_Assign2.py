"""
000859873
Chih-hung Wang
Assignment 1
"""

# a) Ask for the user’s first name.
firstName=input("What is your first name? ")
# b) Ask for the current temperature in Celsius.
temperature=input("What is current Celsius temperature? ")
# c) Make sure it is converted to a float.
celsius=float(temperature)
# d) Convert the temperature to Fahrenheit and print it out to the screen.
# Fahrenheit = (1.8*Celsius) + 32
fahrenheit= (1.8*celsius)+32
print("The Fahrenheit is "+ str(format(fahrenheit,".2f")) + "°F")

# e) If the Temperature (in Celsius):
    # • Is above 21  print “<first name>, it is warm outside.”
    # • Is below 21  print “<first name>, it is cool outside.”
    # • Is 21  print “<first name>, it is perfect outside.”

if celsius > 21:
    print("{0}, it is warm outside.".format(firstName))
elif celsius < 21:
    print("{0}, it is cool outside.".format(firstName))
elif celsius == 21:
    print("{0}, it is perfect outside.".format(firstName))