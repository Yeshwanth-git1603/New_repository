# basic example for multiple inheritance without using consructor

class Base1:
    def method1(self):
        print("Method from Base1")

class Base2:
    def method2(self):
        print("Method from Base2")

class Derived(Base1, Base2):
    def method3(self):
        print("Method from Derived")

# Creating an instance of Derived
obj = Derived()

# Calling methods
obj.method1()  # Method from Base1
obj.method2()  # Method from Base2
obj.method3()  # Method from Derived
