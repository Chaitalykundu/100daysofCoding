######iterator & iterable


l=[1,2,3,4,5,6,7]   #iterable
i=iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for num in (map(lambda a:a**2, l)):
    print(num)
