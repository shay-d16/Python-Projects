# Python:       3.9.4
#
# Author:       Shalondra Rossiter
#
# Purpose:      Create a class that utilizes the concept of abstraction.
#
# Requirements: 1.Your class should contain at least one abstract method and one regular method.  
#               2. Create a child class that defines the implementation of its parents abstract method. 
#               3. Create an object that utilizes both the parent and child methods.
#               4. Create an object that utilizes both the parent and child methods.
#

## ABSTRACT CLASSES

# Abstraction is another fundamental aspect of Object-Oriented programming. 
# Data abstraction hides the complex details of items while only revealing 
# the essential or relevant data. Abstraction hides the complex functionality 
# by creating abstract methods. They are defined, but most of the time do not
# really contain any implementation.

# When a class contains more than one abstract method, it is called an abstract
# class. The implementation of the abstract class is defined by a subclass like
# child class, or a third party plug in. 


## ABC MODULE

# By default, Python does not provide abstract classes. Python comes with a
# module that provides the base for defining Abstract Base classes (ABC) and
# that module is named ABC. ABC works by decorating methods of the base class
# as abstract and then registering concrete classes and implementations of the
# abstract base. A method becomes abstract when decorated with the keyword
# @abstractmethod. (source: geeksforgeeks.org)



from abc import ABC, abstractmethod

class BabyToys(ABC):
    def totalCost(self, amount):
        print("The cost of this toy is: ",amount)
        # This function is telling us to pass in an argument, but we won't tell
        # you how or what kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(BabyToys):
# Here, we've defined how to implement the payment function from its
# parent payment class.
    def payment(self, amount):
        print("You have completed you purchase of {}. Thank you for shopping with Baby Toys America!".format(amount))

pay = DebitCardPayment()
pay.totalCost("$49.99")
pay.payment("49.99")
