# Python:       3.9.4
#
# Author:       Shalondra Rossiter
#
# Purpose:      Create a class that uses encapsulation.
#
# Requirements: 1. This class should make use of a private attribute or function.
#               2. This class should make use of a protected attribute or function.
#               3. Create and object that makes use of protected and private.
#               4. Add comments throughout your Python explaining your code.
#

## PROTECTED VARIABLE


# Protected is prefixed with a *single* underscore. It doesn't actually change
# the behavior of anything though. You could still nodify your methods and
# properties within a class. It acts more as a warninng to other developers
# and basically states that "this is protects - don't use outside of this class"
# without the need for commenting or making it harder to modify your objects.

class UserInfo:
    def __init__(self):
        self._userName = ""

name = UserInfo()
name._userName = "Clarissa McCoy"
print(name._userName)


if __name__ == "__main__":


## PRIVATE VARIABLE

# Private is denoted with a double underscore prefix. It’s harder to access
# but can still be done.


    class UserInfo:
        def __init__(self):
            self.__userPin = 0

        def getPrivate(self):
                print(self.__userPin)

        def setPrivate(self, private):
            self.__userPin = private
                
info = UserInfo()
info.setPrivate(2345)
info.getPrivate()
    
