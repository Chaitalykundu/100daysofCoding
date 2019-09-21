#define a func that takes a no(n)                       (ex:n=3)
#return a dict containing cube of num"s from 1 to n   (ex: {1:1,2:8,3:27}


n=int(input("enter a no: "))
cubes={}
for i in range(1,n+1):
    cubes[i]=i**3
print(cubes)    
