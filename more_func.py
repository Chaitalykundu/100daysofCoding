#WHAT ARE DOC STRING
#HOW TO WRITE DOC STRING
#HOW TO SEE DOC STRING
#WHAT IS HELP FUNCTION

##DOC STRING and HELP FUNC helps to know which func works what##
## we use triple single quotes (''' ''') or triple double quotes (""" """) for docstring

def add(a,b):
    '''this func takes 2 num and return their sum'''
    return a+b
print(add(2,4))

#doc string of this add func:
print(add.__doc__)  #o/p:this func takes 2 num and return their sum


##some doc string
print(len.__doc__)  #o/p:Return the number of items in a container.
print(sum.__doc__)  #o/p:Return the sum of a 'start' value (default: 0) plus an iterable of numbers




############### help func ##############
print(help(sum))    #o/p:sum(iterable, start=0, /)
                    #Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
                    #When the iterable is empty, return the start value.
                    #This function is intended specifically for use with numeric values and may
                    #reject non-numeric types.

print(help(format)) #o/p:Help on built-in function format in module builtins:

                    #format(value, format_spec='', /)
                    #Return value.__format__(format_spec)
    
                    #format_spec defaults to the empty string.
                    #See the Format Specification Mini-Language section of help('FORMATTING') for
                   # details.
