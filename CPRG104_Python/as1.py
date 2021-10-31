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
        self.hand = 0
        self.leg = 4
        self.category="animal"

    def looking(self):
        print("Number of hands: {0}, Number of legs: {1}".format( self.hand,self.leg))

# felines class
class Felines(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.family= "cat family"


    def familyName(self):
        print("Felines belongs to",self.family)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)

# tiger class
class Tiger(Felines):
    def __init__(self):
        Felines.__init__(self)
        self.behaviour="Tigers can roar and are lethal predators\n  "

    def behaivor(self):
        print(self.behaviour)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)
       Tiger.behaivor(self)

# wildCat class
class WildCat(Felines):
    def __init__(self):
        Felines.__init__(self)
        self.behaviour="Wild cats can climb trees\n  "

    def behaivor(self):
        print(self.behaviour)

    def looking(self):
       Animal.looking(self)
       Felines.familyName(self)
       WildCat.behaivor(self)




# canines class
class Canines(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.family= "dog family"

    def familyName(self):
        print("Canines belongs to",self.family)

    def looking(self):
       Animal.looking(self)
       Canines.familyName(self)

# wolf class
class Wolf(Canines):
    def __init__(self):
        Canines.__init__(self)
        self.behaviour="Wolves hunt in packs and have a leader\n "

    def behaivor(self):
        print(self.behaviour)

    def looking(self):
       Animal.looking(self)
       Canines.familyName(self)
       Wolf.behaivor(self)



# bird class
class Bird():
    def __init__(self):
        self.wing = 2
        self.leg = 2

    def looking(self):
        print("Number of wings: {0}, Number of legs: {1}".format( self.wing,self.leg))

# flightBird class
class FlightBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.behaviour="Flight birds fly and hunt for food  "

    def behaivor(self):
        print(self.behaviour)

    def looking(self):
       Bird.looking(self)
       FlightBird.behaivor(self)

# eagle class
class Eagle(FlightBird):
    def __init__(self):
        FlightBird.__init__(self)
        self.behaviours="Eagles fly extremely high and can see their prey from high up in the sky\n "

    def behaivors(self):
        print(self.behaviours)

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






# test file


zoo = Zoo()
zoo.add(Tiger())      # should display animal added
zoo.add(Wolf())      # should display animal added
zoo.add(WildCat())# should display zoo full of animal
zoo.add(Eagle())    # should display bird added
zoo.looking()





