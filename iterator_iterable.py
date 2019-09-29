#iterator vs iterable

n=[1,2,3,4]     #iterables
sq=map(lambda a:a**2, n)    #iterators
print(sq)   #o/p:<map object at ##########>

for i in sq:
    print(i)    #o/p:1
                    #4
                    #9
                    #16
