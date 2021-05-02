# Python:   3.9.4
#
# Author:   Shalondra Rossiter
#

# Purpose:  The purpose of ENCAPSULATION is to wrap your code in one single unit that
#           restricts access from functions and variables from being directly changed
#           or modified by accident within a class.

# Protected is prefixed with a single underscore. It doesn't actually change
# the behavior of anything though. You could still nodify your methods and
# properties within a class. It acts more as a warninng to other developers
# and basically states that "this is protects - don't use outside of this class"
# without the need for commenting or making it harder to modify your objects.


class Protected:
   def __init__(self):
       self._protectedVar = 0

obj = Protected()
obj.protectedVar = 34
print(obj.protectedVar)


class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
