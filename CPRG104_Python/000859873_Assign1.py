"""
000859873
Chih-hung Wang
Assignment 1
"""

# Create a zoo that can have 2 animals and 1 bird.
# Zoo should be able to add only an animal or a bird if it is not full
# Each animal has some common features like the number of hands and legs.
# Felines and canines have 4 legs and no hands
# Each bird has a number of legs and number of wings as a feature.
# Flight birds have 2 legs and 2 wings.
# Dog and cat family and birds belong to animal
# Felines belong to the cat family
# Tiger and cat belong to Felines
# Tigers can roar and are lethal predators
# Wild cats can climb trees
# Canines belong to the dog family.
# Wolves hunt in packs and have a leader
# Wolves belong to the Canines.
# Flight birds belong to the bird family.
# Flight birds fly and hunt for food
# Eagles belongs to Flight birds
# Eagles fly extremely high and can see their prey from high up in the sky.



# aniaml class
from typing import Final
class Animal():
    __hand: Final = 0
    __leg: Final = 4
    def __init__(self):
        self.__hand=Animal.__hand
        self.__leg=Animal.__leg
        

    def looking(self):
        print("Number of hands: {0}, Number of legs: {1}".format(Animal.__hand,Animal.__leg))

# felines class
class Felines(Animal):
    __family: Final = "the cat family"
    def __init__(self):
        Animal.__init__(self)
        self.__family=Felines.__family


    def familyName(self):
        print("Felines belongs to",Felines.__family)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)

# tiger class
class Tiger(Felines):
    __behaviour: Final = "Tigers can roar and are lethal predators\n  "
    def __init__(self):
        Felines.__init__(self)
        self.__behaviour=Tiger.__behaviour

    def behaivor(self):
        print(Tiger.__behaviour)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)
       Tiger.behaivor(self)

# wildCat class
class WildCat(Felines):
    __behaviour: Final = "Wild cats can climb trees\n  "
    def __init__(self):
        Felines.__init__(self)
        self.__behaviour=WildCat.__behaviour

    def behaivor(self):
        print(WildCat.__behaviour)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)
       WildCat.behaivor(self)




# canines class
class Canines(Animal):
    __family: Final = "the dog family"
    def __init__(self):
        Animal.__init__(self)
        self.__family=Canines.__family

    def familyName(self):
        print("Canines belongs to",Canines.__family)

    def looking(self):
       Animal.looking(self)
       Canines.familyName(self)

# wolf class
class Wolf(Canines):
    __behaviour: Final = "Wolves hunt in packs and have a leader\n "
    def __init__(self):
        Canines.__init__(self)
        self.__behaviour=Wolf.__behaviour

    def behaivor(self):
        print(Wolf.__behaviour)

    def looking(self):
       Animal.looking(self)
       Canines.familyName(self)
       Wolf.behaivor(self)



# bird class
class Bird():
    __wing: Final = 2
    __leg: Final = 2

    def __init__(self):
        self.__wing=Bird.__wing
        self.__leg=Bird.__leg

    def looking(self):
        print("Number of wings: {0}, Number of legs: {1}".format(Bird.__wing,Bird.__leg))

# flightBird class
class FlightBird(Bird):
    __behaviour: Final = "Flight birds fly and hunt for food  "
    def __init__(self):
        Bird.__init__(self)
        self.__behaviour=FlightBird.__behaviour

    def behaivor(self):
        print(FlightBird.__behaviour)

    def looking(self):
       Bird.looking(self)
       FlightBird.behaivor(self)

# eagle class
class Eagle(FlightBird):
    __behaviours: Final = "Eagles fly extremely high and can see their prey from high up in the sky\n "
    def __init__(self):
        FlightBird.__init__(self)
        self.__behaviours=Eagle.__behaviours

    def behaivors(self):
        print(Eagle.__behaviours)

    def looking(self):
       FlightBird.looking(self)
       Eagle.behaivors(self)


# zoo class
class Zoo():

    def __init__(self):
        self.list=[]



    def add(self,type):
        self.list.append(type)

        result_animal = 0
        result_bird = 0
        for i in self.list:
            if isinstance(i,Animal):
                result_animal += 1



            elif isinstance(i,Bird):
                result_bird+=1

        if isinstance(type,Animal):
            if result_animal<=2:
                print("Animal Added")
            else:
                print("Zoo full of animals")
        elif isinstance(type,Bird):
            if result_bird<=1:
                print("Bird Added")
            else:
                print("Zoo full of Birds")



    def looking(self):
        result_animal = 0
        result_bird = 0
        for i in self.list:
            if isinstance(i, Animal):
                result_animal += 1
                if result_animal<=2:
                    i.looking()


            elif isinstance(i, Bird) :
                result_bird += 1
                if result_bird <= 2:
                    i.looking()






# test


zoo = Zoo()
zoo.add(Tiger())      # should display animal added
zoo.add(Wolf())      # should display animal added
zoo.add(WildCat())# should display zoo full of animal
zoo.add(Eagle())    # should display bird added
zoo.looking()





