# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Complete these actions
#

### 1. Create a tuple and print it.
queenTuple = ("Bohemian Rhapsody", "Killer Queen", "Don't Stop Me Now", \
              "Somebody To Love", "Bohemian Rhapsody")
print("These are some of my favorite songs by Queen!\n")


### 2. Loop through the tuple items by using a for loop.
for i in queenTuple:
    print(i)


### 3. Use the count() method on a tuple.
x = queenTuple.count("Bohemian Rhapsody")
print("\nOops! I just realized I added \"Bohemian Rhapsody\" to my tuple {} times!".format(x))
                     
