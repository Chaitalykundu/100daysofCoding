#map function

num=[1,2,3,4]

def sq(a):
    return a**2
print(map(sq,num))  #o/p:<map object at 0x03C1B890>
sqs=list(map(sq,num))
print(sqs)  #o/p:[1, 4, 9, 16]


#lambda func
squares=list(map(lambda a:a**2,num))
print(squares)   #o/p:[1, 4, 9, 16]

#list comp
sq_new=[i**2 for i in num]
print(sq_new)    #o/p:[1, 4, 9, 16]

##other
name="äbc","defg","uvwxyz"
length=list(map(len,name))
print(length)   #o/p:[3, 4, 6]


