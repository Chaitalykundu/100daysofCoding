def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print("this is awesome")
        return any_func(*args, **kwargs)
    return wrapper_func

@decorator_func

def func(a):
    print(f"this is func with argument {a}")

func(5)     #o/p:this is func with argument 5


@decorator_func
def add(a,b):
    return a+b

print(add(2,7)) #o/p:9


            ## output: this is awesome
                        #this is func with argument 5
                        #this is awesome
                        #9

