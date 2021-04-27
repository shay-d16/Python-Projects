# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Create two classes that inherit from another class as part of 
# Inheritance Submission Assignment given to me by the Tech Academy
# Requirements:
# 1. Ensure each child has at least two of their own attributes
# 2. Add comments throughout your Python explaining you code.
#


## CREATING A CLASS IN PYTHON

    # You use the keyword Class, and then variable names for the attributes. 
    # As part of the definition, you also need to give default values.
    # These values can change with each object so long as we provide methods 
    # to do so. The methods would be defined like any other function. 
    # These methods, however, only belong to this class.


    # The methods will need the elements of the class to operate, so you use the 
    # 'self' keyword to pass them into the function. The self keyword represents an 
    # instance (object) of the class, its attributes and functions.
    # You can call the elements using self.element

class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

## CREATING A CLASS WITH ARGUMENTS
    
        # For creating a new class, it is useful to be able to pass in all
        # the values for the attributes at the time the object is created. 
        # This is called initialization and can easily be set up. It just  
        # requires utilizing a dunder method (__init__ ) to attach the
        # arguments for creating the object to the attributes of that object. 
        # You’ll create a new user from the User class created above.
        # First add the following dunder method to the definition of the class.
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
        # This is all that is needed for defining the initialization.
        # The def __init__() needs to be as the attributes of the class
        # so that it will be part of the class definition

    # Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

## INHERITANCE
            
    # Inheritance is one of the primary concepts of object-oriented programming.
    # In some cases, you may want all the attributes and methods of a class,
    # but with additional information that doesn’t necessarily belong to the
    # original class.  
    # The concept is that in some cases you may want to add additional attributes 
    # or methods to a class without having to either completely duplicate the class
    # or modify the existing class. This would be creating a “child” of a class 
    # and would inherit all the properties and functions of the parent class.

        # In this particular example, you will probably want to track basic
        # attributes like name, email, address,etc. about all users for your site.
        # However, if you have employees and customers using a site, there are  
        # probably additional attributes you want to track for each that don’t 
        # overlap. To make the code as concise as possible, you’d want to have 
        # a parent class of User for the attributes and methods common to both.
        # You would also want a child class class for Employee and Customer that 
        # track the additional attributes and methods for those objects.
    
class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ''
    mailing_list = True
    # Employee and Customer are now child classes with their own added  
    # attributes that are unique to them as they’ve inherited all attributes
    # from their their parent class User without having to retype everything. 
    # This saves memory, time and space in your code. 



# Outside of the class you would create an instance of the User class:
# new_user = User()

# Call the login method using the new object:
# new_user.login()

