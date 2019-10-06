###########  ADVANCE MIN() MAX() ##############

#NORMAL METHOD
n=[1,2,3,4,5]
print(min(n))
print(max(n))


#advance
def func(items):
    return len(items)
names=["moni","chaitaly"]
print(min(names,key=func))
print(max(names,key=func))

#using lambda func
name=["moni","chaitaly"]
print(max(name,key=lambda item : len(item)))
print(min(name,key=lambda item : len(item)))


### using list##
# according to score
std=[
    {"name":"moni","score":90,'age':19},
    {"name":"monisha","score":95,'age':18},
    {"name":"chaitaly","score":88,'age':20}
    ]
print(max(std,key=lambda info:info.get('score')))    #o/p:{'name': 'monisha', 'score': 95, 'age': 18}
print(min(std,key=lambda info:info.get('score')))   #o/p:{'name': 'chaitaly', 'score': 88, 'age': 20}

#according to age
print(max(std,key=lambda info:info.get('age'))) #o/p:{'name': 'chaitaly', 'score': 88, 'age': 20}
print(min(std,key=lambda info:info.get('age'))) #o/p:{'name': 'monisha', 'score': 95, 'age': 18}



### using dict ##
std1={
    "moni":{"score":90,'age':19},
    "monisha":{"score":95,'age':18},
    "chaitaly":{"score":88,'age':20}
    }
print(max(std1,key=lambda info: std1[info]['age'])) #o/p:chaitaly
print(min(std1,key=lambda info: std1[info]['age'])) #o/p:monisha
