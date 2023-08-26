#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,breed):
        self.breed=breed
        self._name=name


    def get_name(self,breed):
        return self._name and self.breed

    def set_name(self,name,breed):
        if(type(name)in (str)) and  (1 >= name <=25 ):
            pass

        else:
            print("Name must be string between 1 and 25 characters.")


        self._name=name



    name=property(set_name(),get_name(),)
    breed=property(set_name(),get_name())
