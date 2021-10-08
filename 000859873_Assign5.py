"""
SAIT ID:000859873
Author:Chih-hung Wang
Assignment 5
purpose:
•	This assignment takes the story “Henry the Square Eared Cat” and changes it to “Henry the Pentagon Eared Cat.”
You are required to write a program that reads the story, finds all the words “square,” and replace them with the word “pentagon”.

"""

import os

path = os.path.dirname(__file__)
filePath = os.path.join(path, "./henryTheSquareEaredCat.txt")
file = open(filePath, "r")

newFilePath = os.path.join(path, "./henryThePentagonEaredCat.txt")
newFile=open(newFilePath,"w")

for line in file:
    newFile.write(line.replace("Square","Pentagon").replace("square","pentagon"))

print("Created henryThePentagonEaredCat.txt” file")
file.close()
newFile.close()

choice=input("Do you want to keep the newly generated file “henryThePentagonEaredCat.txt”?(y or n) ")
if choice=="n":
    os.remove(newFilePath)
    print("Remove henryThePentagonEaredCat.txt” file")
elif choice=="y":
    print("Enjoy your henryThePentagonEaredCat.txt” file")




