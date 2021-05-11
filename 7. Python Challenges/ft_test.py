# Python:   Version 3.9.4
#
# Author:   Shalondra Rossiter
#
# Purpose:  
#
#

# The shutil module provides a way for a developer to perform various
# functions on a single or grouped file. You can use it to transfer files
# from a location on your computer to another, as well as copy and delete files.

import shutil
import os

# Set where the source of the files are
source = 'C://Users/USER/OneDrive/Documents//GitHub/Python-Projects/7. Python Challenges/folderA/'

# Set the destination path to folderB
destination = 'C:/Users//USER/OneDrive/Documents/GitHub/Python-Projects/7. Python Challenges/folderB/'
files = os.listdir(source)

for i in files:
    # We are saying move the files represented by i to their new destination.
    shutil.move(source+i, destination)
