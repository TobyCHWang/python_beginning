"""
SAIT ID:000859873
Author:Chih-hung Wang
Assignment 4
purpose:
•	ask the user for their first name
•	ask the user to select any variety of toppings for a pizza
•	calculate the total cost of the pizza
•	print a message to the user summarizing their pizza order

"""

name = input("What is your last name? ")
def items(key):
    if (key == 1):
        return "Cheese"
    elif (key == 2):
        return "Pineapple"
    elif (key == 3):
        return "Pepperoni"
    elif (key == 4):
        return "Ham"
    elif (key == 5):
        return "Everything"
    else:
        return "Done"
# Define a dictionary
extras = {1:8,2:10,3:12,4:14,5:14,6:False}
keys = list(extras)
topping ={1:"Cheese ",2:"Pineapple ",3:"Pepperoni ",4:"Ham ",5:"Everything "}
# Ask the user for toppings until they select "Done"
tally = 0
toppingItem=0
choosing = True
text=""

while (choosing):
    for i in range(0, len(keys)):
        x = keys[i]
        print(str(x) + ".) " + items(x))
    choice = input("Choose a topping: ")
    if (int(choice) == 6):
        choosing = extras[6]
    elif (int(choice) == 5):
        choosing = False
        tally =  extras[5]
        text += topping[int(choice)]
    else:
        toppingItem += 1
        text += topping[int(choice)]


    if(toppingItem==1):
        tally=extras[1]
    elif(toppingItem==2):
        tally=extras[2]
    elif(toppingItem==3):
        tally=extras[3]
    elif(toppingItem==4):
        tally = extras[5]

    keys.remove(int(choice))
# Summary
print("Hello, "+ name)
print("Selected topping list: "+ text)
print("Your total comes to: ${:.2f}".format(tally,2))



