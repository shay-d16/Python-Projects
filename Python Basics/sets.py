# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Complete these actions as part of a challenge 
# given to me by the Tech Academy.
#


# Sets are used to store multiple items in a single variable. A set is
# a collection which is both *unordered* and *unindexed*. They are
# written with curly brackets




### 1. Create a set.
mySet = {"Honey Buns", "Brownies", "Vanilla Ice Cream", "Dutch Apple Pie"}
print(mySet)


### 2. Add an item to a set using th add() method
mySet.add("Ruby Chocolate")
mySet.add("Dove Milk Chocolate")
print(mySet)


### 3. Use the remove() method to take an item out of a set.
mySet.remove("Dove Milk Chocolate")
print(mySet)


### 4. Use the difference() method on a set.
newSet = {"Honey Buns", "Vanilla Ice Cream", "Strawberry Cheesecake", "Dutch Apple Pie"}
x = mySet.difference(newSet)    # The difference() method returns a set that
print(x)                        # contains the difference between two sets.
