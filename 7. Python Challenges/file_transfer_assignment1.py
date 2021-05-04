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
source = 'folderA'

# Set the destination path to folderB
destination = 'folderB'
files = os.listdir(source)

for i in files:
    # We are saying move the files represented by i to their new destination.
    shutil.move(source+i, destination)
