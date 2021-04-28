# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Learn how to write your own classes, and write object-
# oriented programming
#



class Game:
    variable1 = 'Hello'
    variable2 = 'World!'
    # All that's been done so far is define a class 'Game' and simply 
    # stated the blueprints to make this class 'Game'
    # These are the attributes and values of the 'Game' object. 
    # This information doesn't do anything by itself. You have to first
    # instantiate, which means it uses those blueprints to build and
    # bring the the 'Game' object into being. 
    # 


















if __name__ == "__main__":
    x = Game()
    # Because you can have multiple instantiations of a class object,
    # you have to make sure you give the instantiation a name.
    # Now you can call it by 'x' instead of 'Game'.
    print("{} {}".format(x.variable1,x.variable2))
    # This calls the values within 'variable1' and 'variable2'of 
    # the 'Game' object using the format method.
