"""
000859873
Chih-hung Wang
Assignment 2
"""

# For this assignment, your goal is to anticipate and handle exceptions that may occur in a program.
# This assignment is designed to measure and assess your ability to:
# Understand and handle a variety of exceptions thrown by the program.
# Consider how exceptions are used to enforce validations.
# Design and use simple regular expressions
# Create and use lambdas and higher order functions.




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

# exception
class NumberError(Exception):
    pass
# exception
class AddError(Exception):
    pass

# zoo class
class Zoo():

    def __init__(self):
        self.list=[]


    def add(self,type):
        if not isinstance(type,(Animal,Bird)):
             raise TypeError("{0} doesn't belong to Animal and Bird class!!!".format(type))

        try:
            self.list.append(type)
            result_animal = 0
            result_bird = 0
            # filter tiger
            tiger = filter(lambda tiger:isinstance(tiger,Tiger), self.list)
            count_tiger = len(list(tiger))
            # filter wild cat
            wildcat = filter(lambda wildcat:isinstance(wildcat,WildCat), self.list)
            count_wildcat = len(list(wildcat))

            # filter wolf
            wolf = filter(lambda wolf:isinstance(wolf,Wolf), self.list)
            count_wolf = len(list(wolf))

            # filter eagle
            eagle = filter(lambda eagle:isinstance(eagle,Eagle), self.list)
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

        # exception
        except NumberError:
            print("Error in adding animal/bird")
        except AddError:
            print("Animal already exists")
        # else
        else:
            print("Added successfully\n")





    def looking(self):

        # animal
        animal_filter=filter(lambda animal:isinstance(animal,Animal),self.list)
        animal_lst=(list(animal_filter))


        # bird
        bird_filter = filter(lambda bird:isinstance(bird,Bird), self.list)
        bird_lst = (list(bird_filter))


        # map
        # def map_filt(a):
        #     if isinstance(a,Animal):
        #         return 1
        #     elif isinstance(a,Bird):
        #         return 2

        # tiger_map = map(lambda map_tiger: "Tiger" if isinstance(map_tiger, Tiger) else "No", self.list)
        animal_map_lst=map(lambda map_filter:1 if isinstance(map_filter,Animal)
                           else(2 if isinstance(map_filter,Bird) else 66), self.list)
        bird_map_lst =map(lambda map_filter:1 if isinstance(map_filter,Animal)
                           else(2 if isinstance(map_filter,Bird) else 66), self.list)

        # map filter

        # def map_animal(a):
        #     if a==1:
        #         return True
        #
        # def map_bird(a):
        #     if a==2:
        #         return True

        map_animal_filter=filter(lambda map_animal:True if map_animal==1 else False,animal_map_lst)
        map_animal_filter_list = list(map_animal_filter)

        map_bird_filter = filter(lambda map_animal:True if map_animal==2 else False, bird_map_lst)
        map_bird_filter_list = list(map_bird_filter)



        # reduce

        map_animal_filter_list.append(0)
        map_bird_filter_list.append(0)

        result_animal=functools.reduce(lambda acc,ele:acc+1,map_animal_filter_list)
        result_bird =functools.reduce(lambda acc,ele:acc+1, map_bird_filter_list)



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


      canine_filter_l = filter(lambda canine:isinstance(canine,Canines), self.list)
      canine_filter_list=list(canine_filter_l)

      def look_at_member(listOfObjects):
          for i in listOfObjects:
              print(i.looking())

      look_at_member(canine_filter_list)

# find_tiger
    def find_tiger(self):
        # def map_tiger(a):
        #     if isinstance(a, Tiger):
        #         return "Tiger"
        #     else:
        #         return "No"

        tiger_map=map(lambda map_tiger:"Tiger" if isinstance(map_tiger,Tiger) else "No",self.list)
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
# zoo.add(Tiger())
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





