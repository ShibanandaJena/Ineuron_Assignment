from abc import ABC, abstractmethod

# #1.Demonstrate use of abstract class
class AbstractClass(ABC):
    @abstractmethod # This is an abstract method
    def abstract_method(self):
        pass

class abstract_check(AbstractClass): # This is a concrete class
    def abstract_method(self): # This is a concrete method
        print("Abstract method implementation") 

class abstract_check2(AbstractClass): # This is another concrete class
    def abstract_method(self): # This is another concrete method
        print("Abstract method implementation")

check_one = abstract_check()
check_one.abstract_method()

check_two = abstract_check2()
check_two.abstract_method()


# # 2. use of multiple inheritance in python

class A:        # Base class
    def m(self):
        print("A")
       
class B(A):      # Derived class (inherits from A)
    def m(self):
        print("B")
 
class C(A):        # Derived class (inherits from A)
    def m(self):
        print("C") 
        
class D(B, C):      # Derived class (inherits from B and C)
    pass  
     
obj = D()          # Create an object of D
obj.m()            # Call method m of D


# 3. Use of decorator in python

def decorator(function_main):
 
    # inner_function is a Wrapper function in
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner_function():
        print("Hello, this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        function_main()
 
        print("This is after function execution")
         
    return inner_function
 
 
# defining a function, to be called inside wrapper
def main_function_to_be_used():
    print("This is inside the function !!")
 
 
# passing 'main_function_to_be_used' inside the
# decorator to control its behaviour
main_function_to_be_used = decorator(main_function_to_be_used)
 
 
# calling the function
main_function_to_be_used()