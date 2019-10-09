#ANY ALL FUNC
def sum(*args):
    
    if all([(type(arg)== int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "Wrong input"
print(sum(1,2,3,4,5,'moni'))    #o/p:Wrong input
print(sum(1,2,3,4,5))       #o/p:15
