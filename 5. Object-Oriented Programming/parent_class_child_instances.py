# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: More on 'parent' and 'child' classes
#

## PARENT CLASS
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = 0
    arms = 0
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True
    # Now that you've defined this class and set the basic outline
    # you can give this class object a method
    
    # Methods within this class block stay on the same indention level
    # as the attributes inside this class.
    def information(self):
        # The self parameter is a reference to the current instance of 
        # the class,  and is used to access variables that belongs to 
        # the class. It does not have to be named self, you can call it
        # whatever you like, but it has to be the first parameter of
        # any function in the class.
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        # Remember that even though the attributes in the string have
        # capital letters, the actual variables are lowercase so you
        # would have to use lowercase for the program to run.
        # Variables are case-sensitive.
        return msg

## CHILD CLASS INSTANCE
class Human(Organism):
    name = "MacGuyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum and a roll of duct tape!"
        return msg

## ANOTHER CHILD CLASS INSTANCE
    class Dog(Organism):
        name = "Spot"
        species = "Canine"
        legs = 4
        arms = 0
        dna = "Sequence B"
        origin = "Earth"

        def bite(self):
            msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
            return msg

## ANOTHER CHILD INSTANCE
    class Bacterium(Organism):
        name = "X"
        species = "Bacteria"
        legs = 0
        arms = 0
        dna = "Sequence C"
        origin = "Mars"

        def replication(self):
            msg = "\nThe cells begin to divide and multiply into two separate organisms!"
    
            



if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
          
    # Here you are instatiating a 'Human' object, a 'Dog' object
    # and a 'Bacterium' object, and then calling in the inherited
    # information() method that they all posses, and then call on
    # each of their specific methods. You have already overrid
    # certain information that will take place
    # Once they are instatiated, even though they inherited
    # these values, you can override these values 
