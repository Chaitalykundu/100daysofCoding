####generator: if we want to use any sequence once, we can use generator

###needed::
    # 1) generator function
    # 2) generator comprehension


#############  generator func #####################
#           --------------------------------

#normal func:
def num(n):
    for i in range(0,n+1):
        print(i)
num(10)


#using generator:
def num(n):
    for i in range(0,n+1):
        yield(i)
print(num(10))  #o/p:<generator object num at 0x02E44338>

for nums in num(10):
    print(nums)

#N.B: yield is used to create generator
