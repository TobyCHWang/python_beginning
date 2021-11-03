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

class Animal():
    def __init__(self):
        self.__hand = 0
        self.__leg = 4


    def looking(self):
        return (("Number of hands: {0}, Number of legs: {1}".format( self.__hand,self.__leg))+"\n")

# felines class
class Felines(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__family= "Felines belongs to the cat family\n"


    def getFamilyName(self):
        return self.__family

    def looking(self):
       return (Animal.looking(self)+Felines.getFamilyName(self))


# tiger class
class Tiger(Felines):
    def __init__(self):
        Felines.__init__(self)
        self.__behaviour="Tigers can roar and are lethal predators\n  "

 
    def getBehaivor(self):
        return self.__behaviour

    def looking(self):
       return (Felines.looking(self)+Tiger.getBehaivor(self))

#Please consider all the above comments and address them in the following classes
# wildCat class
class WildCat(Felines):
    def __init__(self):
        Felines.__init__(self)
        self.__behaviour="Wild cats can climb trees\n  "

    def getBehaivor(self):
        return self.__behaviour

    def looking(self):
       return (Felines.looking(self)+WildCat.getBehaivor(self))




# canines class
class Canines(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__family= "Canines belongs to the dog family\n"

    def getFamilyName(self):
        return self.__family

    def looking(self):
       return (Animal.looking(self)+Canines.getFamilyName(self))


# wolf class
class Wolf(Canines):
    def __init__(self):
        Canines.__init__(self)
        self.__behaviour="Wolves hunt in packs and have a leader\n "

    def getBehaivor(self):
        return self.__behaviour

    def looking(self):
       return (Canines.looking(self)+Wolf.getBehaivor(self))



# bird class
class Bird():
    def __init__(self):
        self.__wing = 2
        self.__leg = 2

    def looking(self):
        return (("Number of wings: {0}, Number of legs: {1}".format( self.__wing,self.__leg))+"\n")

# flightBird class
class FlightBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.__behaviour="Flight birds fly and hunt for food\n"

    def getBehaivor(self):
        return self.__behaviour

    def looking(self):
       return (Bird.looking(self)+FlightBird.getBehaivor(self))


# eagle class
class Eagle(FlightBird):
    def __init__(self):
        FlightBird.__init__(self)
        self.__behaviours="Eagles fly extremely high and can see their prey from high up in the sky "

    def getBehaivor(self):
        return (self.__behaviours)

    def looking(self):
       return (FlightBird.looking(self)+Eagle.getBehaivor(self))



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
                    print(i.looking())


            elif isinstance(i, Bird) :
                result_bird += 1
                if result_bird <= 2:
                    print(i.looking())






# test


zoo = Zoo()
zoo.add(Tiger())      # should display animal added
zoo.add(Wolf())      # should display animal added
zoo.add(WildCat())# should display zoo full of animal
zoo.add(Eagle())    # should display bird added
zoo.looking()





