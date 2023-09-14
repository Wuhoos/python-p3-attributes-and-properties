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
    def __init__(self, name ='Fido' , breed = "Corgi"):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) is str) and (1 <= len(name) <= 25):
            self._name = name
        else: 
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed_parameter):
        if not (breed_parameter in APPROVED_BREEDS):
            print('Breed must be in list of approved breeds.')
        self._breed = breed_parameter
        