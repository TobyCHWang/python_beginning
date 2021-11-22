"""
000859873
Chih-hung Wang
Assignment 2
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
import functools
import re


class Toby():
    def __init__(self):
        self.__hand = 0
        self.__leg = 4


    def looking(self):
        return (("Number of hands: {0}, Number of legs: {1}".format( self.__hand,self.__leg))+"\n")

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

class NumberError(Exception):
    pass

class AddError(Exception):
    pass

# zoo class
class Zoo():

    def __init__(self):
        self.list=[]

    # tiger
    def tiger(self,tiger):
        if isinstance(tiger, Tiger):
            return True

    # wild cat
    def wildcat(self,wildcat):
        if isinstance(wildcat, WildCat):
            return True
    # wolves
    def wolf(self, wolf):
        if isinstance(wolf, Wolf):
            return True

    # eagle
    def eagle(self, eagle):
        if isinstance(eagle,Eagle):
            return True

    def add(self,type):
        if not isinstance(type,(Animal,Bird)):
             raise TypeError("{0} doesn't belong to Animal and Bird class!!!".format(type))

        try:
            self.list.append(type)
            result_animal = 0
            result_bird = 0
            # filter tiger
            tiger = filter(self.tiger, self.list)
            count_tiger = len(list(tiger))
            # filter wild cat
            wildcat = filter(self.wildcat, self.list)
            count_wildcat = len(list(wildcat))

            # filter wolf
            wolf = filter(self.wolf, self.list)
            count_wolf = len(list(wolf))

            # filter eagle
            eagle = filter(self.eagle, self.list)
            count_eagle = len(list(eagle))

            if count_tiger > 1:
                self.list.remove(type)
                raise AddError
            elif count_wildcat > 1:
                self.list.remove(type)
                raise AddError
            elif count_wolf>1:
                self.list.remove(type)
                raise AddError
            elif count_eagle>1:
                self.list.remove(type)
                raise AddError

            for i in self.list:
                if isinstance(i, Animal):
                    result_animal += 1

                elif isinstance(i, Bird):
                    result_bird += 1

            if isinstance(type, Animal):
                if result_animal > 2:
                    raise NumberError
            elif isinstance(type, Bird):
                if result_bird > 1:
                    raise NumberError


        except NumberError:
            print("Error in adding animal/bird")
        except AddError:
            print("Animal already exists")
        else:
            print("Added successfully\n")





    def looking(self):



        def animal(a):
                if isinstance(a, Animal):
                    return True

        def bird(a):
                if isinstance(a, Bird):
                    return True

        # animal
        animal_filter=filter(animal,self.list)
        animal_lst=(list(animal_filter))


        # bird
        bird_filter = filter(bird, self.list)
        bird_lst = (list(bird_filter))


        # map
        def map_filt(a):
            if isinstance(a,Animal):
                return 1
            elif isinstance(a,Bird):
                return 2
        animal_map_lst=map(map_filt, self.list)
        bird_map_lst =map(map_filt, self.list)

        # map filter

        def map_animal(a):
            if a==1:
                return True

        def map_bird(a):
            if a==2:
                return True

        map_animal_filter=filter(map_animal,animal_map_lst)
        map_animal_filter_list = list(map_animal_filter)

        map_bird_filter = filter(map_bird, bird_map_lst)
        map_bird_filter_list = list(map_bird_filter)



        # reduce
        def calc(acc, ele):
             return acc + 1

        map_animal_filter_list.append(0)
        map_bird_filter_list.append(0)

        result_animal=functools.reduce(calc,map_animal_filter_list)
        result_bird =functools.reduce(calc, map_bird_filter_list)



        if result_animal<=2:
            for i in animal_lst:
                print(i.looking())
        else:
            list_keep_first_two=animal_lst[0:2]
            for i in list_keep_first_two:
                print(i.looking())

        if result_bird<=2:
            for i in bird_lst:
                print(i.looking())
        else:
            bird_lst_keep_first_two=bird_lst[0:1]
            for i in bird_lst_keep_first_two:
                print(i.looking())




# find_canine method
    def find_canine(self):
      def canine_filter(a):
         if isinstance(a, Canines):
              return True

      canine_filter_l = filter(canine_filter, self.list)
      canine_filter_list=list(canine_filter_l)

      def look_at_member(listOfObjects):
          for i in listOfObjects:
              print(i.looking())

      look_at_member(canine_filter_list)

# find_tiger
    def find_tiger(self):
        def map_tiger(a):
            if isinstance(a, Tiger):
                return "Tiger"
            else:
                return "No"

        tiger_map=map(map_tiger,self.list)
        tiger_map_list=list(tiger_map)


        for i in tiger_map_list:
            tiger_match=re.search("Tiger",i)
            if tiger_match:
                index=tiger_map_list.index("Tiger")
            else:
                index="No"

        if index=="No":
            print("")
        else:
            tiger_obj=self.list[index]
            print(tiger_obj.looking())













# test


zoo = Zoo()
zoo.add(Wolf())
zoo.looking()

zoo.find_canine()
zoo.find_tiger()


# # zoo.add(Wolf())
# zoo.add(Tiger())
#
# # zoo.find_tiger()
# #
# # zoo.find_canine()
#
# # zoo.add(Tiger())
# zoo.add(WildCat())
# # zoo.add(WildCat())# should display animal added
# zoo.add(Wolf())
# zoo.add(Eagle())
# # zoo.add(Eagle())
# # zoo.find_canine()
# zoo.looking()
# # # should display animal added
# # # zoo.add(WildCat())# should display zoo full of animal
# #     # should display bird added
#
# # zoo.add(Toby())





