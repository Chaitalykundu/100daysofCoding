#iterator vs iterable
###tuples,string are iterables

n=[1,2,3,4]     #iterables
sq=map(lambda a:a**2, n)    #iterators
print(sq)   #o/p:<map object at ##########>


print(next(sq)) #o/p:1
print(next(sq)) #o/p:4
print(next(sq)) #o/p:9
print(next(sq)) #o/p:16


##using for loop::::::::
for i in sq:
    print(i)    #o/p:1
                    #4
                    #9
                    #16

#print(next(n))  #o/p:Error,,('list' object is not an iterator)
print(iter(n))  #o/p:<list_iterator object at 0x02E3B8F0> (thats iterator is a object)






#######HOW FOR LOOP ACTUALLY WORKS#######
#step call iter function
#iter(n)---> iterator
#next(iter(n))
    
nmb=[1,2,3,4]
nm_iter=iter(nmb)
print(next(nm_iter))    #O/P:1
print(next(nm_iter))    #O/P:2
print(next(nm_iter))    #O/P:3
print(next(nm_iter))    #O/P:4
#print(next(nm_iter))    #O/P:StopIteration

