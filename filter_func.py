#filter function

def even(a):
    return a%2==0
number=list(range(1,11))
print(number)   #o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n=filter(even,number)
print(n)    #o/p:<filter object at 0x030EB8D0>

evens=tuple(filter(even,number))
print(evens)    #o/p:(2, 4, 6, 8, 10)


even_no=list(filter(lambda i:i%2==0,number))
print(even_no)  #o/p:[2, 4, 6, 8, 10]
