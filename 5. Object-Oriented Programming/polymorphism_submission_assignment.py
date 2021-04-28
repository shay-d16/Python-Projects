# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Complete and submit this assignment given to me by the 
# Tech Academy
#
# Requirements: Create two classes that inherit from another class
# 1. Each child should have at least two of their own attributes
# 2. The parent class should have at least one method (function)
# 3. Both child classes should utilize polymorphisms on the parent 
#    class method
# 4. Add comments throughout your Python explaining your code
#

## PARENT CLASS FAIRY
class Fairy():
    name = "Queen Clarion"
    species = "Never Fairy"
    location = "Pixie Hollow"
    
    

    def getFairyInfo(self):
        getName = self.name
        getSpecies = self.species
        getLocation = self.location
        msg = ("\nName: {}\nSpecies: {}\nLocation: {}".format(self.name,self.species,self.location))
        print(msg)

##CHILD CLASS TINKERFAIRY
class TinkerFairy(Fairy):
    name = "Tinker Bell"
    talent = "Tinker-talent"
    home = "Tinker's Nook"

    # This is the same method in the parent class 'Fairy', but instead
    # of using 'species' and 'location', we're using 'talent' and 'home'.
    def getFairyInfo(self):
        getName = self.name
        getTalent = self.talent
        getHome = self.home
        msg = ("\nName: {}\nTalent: {}\nHome: {}".format(self.name,self.talent,self.home))
        print(msg)

## CHILD CLASS GARDENFAIRY
class GardenFairy(Fairy):
    name = "Rosetta"
    talent = "Garden-talent"
    home = "Spring Valley"

    def getFairyInfo(self):
        getName = self.name
        getTalent = self.talent
        getHome = self.home
        msg = ("\nName: {}\nTalent: {}\nHome: {}".format(self.name,self.talent,self.home))
        print(msg)

# The following code invokes the methods inside each class
queen = Fairy()
queen.getFairyInfo()

tinker = TinkerFairy()
tinker.getFairyInfo()

garden = GardenFairy()
garden.getFairyInfo()
