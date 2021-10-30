"""
000859873
Chih-hung Wang
Assignment 3
for loop Print the song 99 Bottles of Beer on the Wall to the screen
http://www.99-bottles-of-beer.net/lyrics.html
"""

for i in range(100, 0, -1):
    if (i == 1):
        print(
            " {0} bottle of beer on the wall,\n {0} bottle of beer!\n Take it down,\n Pass it around,\n No more bottles of beer on the wall!".format(
                i))
    elif (i == 2):
        print(
            " {0} bottles of beer on the wall,\n {0} bottles of beer!\n Take one down,\n Pass it around,\n {1} bottle of beer on the wall!\n".format(
                i, i - 1))

    else:
        print(
            " {0} bottles of beer on the wall,\n {0} bottles of beer!\n Take one down,\n Pass it around,\n {1} bottles of beer on the wall!\n".format(
                i, i - 1))