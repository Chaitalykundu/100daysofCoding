########### PASS FUNC AS ARGUMENTS ############

#map:
def sq(a):
    return a**2
l=[1,2,3,4]
print(list(map(sq,l)))  #o/p:[1, 4, 9, 16]

def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(sq,l))      #o/p:[1, 4, 9, 16]   #(sq & l are defined)



#lambda:
b=[1,2,3,4,5]
print(list(map(lambda c:c**2,b)))   #o/p:[1, 4, 9, 16, 25]
print(map(lambda c:c**2,b)) #o/p:<map object at 0x0386CAB0>
print(lambda c:c**2,b)  #o/p:<function <lambda> at 0x031FBED0> [1, 2, 3, 4, 5]
