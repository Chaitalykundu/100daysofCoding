########## DECORATORS #########
#decorators: enhance the functionality of other functions
# @(syntactic sugar) is used for decorator

def func1():
    print("this is function 1")

def func2():
    print("this is function 2")
    
func1() #o/p:this is function 1
func2() #o/p:this is function 2


## decorator:
#-----------------
def decorator_func(any_func):
    def wrapper_func():
        print("this is awesome")
        any_func()
    return wrapper_func()

def func3():
    print("this is function 3")

def func4():
    print("this is function 4")

v=decorator_func(func3) #o/p:this is awesome
                        #this is function 3


## using syntactic sugar (this is sort cut way):
#---------------------------------------------------
def decorator_function(any_function):
    print("this is awesome")
    any_function()
        
@decorator_function
def func3():
    print("this is function 3")  #o/p:this is awesome
                                 #this is function 3


