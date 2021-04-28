# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: The word 'polymorphism' means 'having many forms,'
# and it is an extension of the concept of inheritance. It 
# essentially breaks down into a child class being able to 
# override the behavior of the parent class; polymorphism
# let the child classes keep the same function names of
# thier parents but can modify their functionality
#

## PARENT CLASS USER
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your passowrd: ")
        if(entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

## CHILD CLASS EMPLOYEE
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    # This is the same method in the parent class 'User'. The difference
    # is that, instead of using entry_password, we're using entry_pin
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your passowrd: ")
        if(entry_email == self.email and entry_password == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

# The following code invokes the methods inside each class for 'User' and 'Employee'
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

# This is an example of polymorphism
# You have child classes that perform the same function in different ways.
