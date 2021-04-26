# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# These are some challenges given to my by The Tech Academy that
# focus on operators in Python.


### Assignment Operator
x = 10
y = 15



### Arithmetic Operator
print(x + y)  # This adds the values of x and y together and prints the answer



### Comparison Operator
print(x != y)  # This checks to see if the statement is true/false; x is NOT
               # equal to y. This is true so it would print 'True'.


### Logical Operator
print(x > 5 and y < 14) # 'And' operator checks to see if *both* comparisons are true
                        # but only one of the comparisons is true, therefore making
                        # making the entire statement false, so it prints 'False'.



### Identity Operator
print(x is not y)   # Identity operators are used to compare the objects, not if 
                    # they are equal, but if they are actually the same object, with
                    # the same memory location. In this case, it would print 'True'.


### Bitwise Operator
b = bin(11) # The bin() function returns the binary version of a specified integer.
c = bin(12)
print(0b1011 | 0b1100)  # '&' operator 

