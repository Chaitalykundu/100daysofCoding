#### ADVANCE SORT METHOD #####

#normal sort
fruits=['mango','apple','banana']
fruits.sort()
print(fruits)   #o/p:['apple', 'banana', 'mango']



#sort according to score
std=[
    {"name":"moni","score":90,'age':19},
    {"name":"monisha","score":95,'age':18},
    {"name":"chaitaly","score":88,'age':20}
    ]
s=sorted(std,key=lambda d:d['score'])
print(s)  #o/p:[{'name': 'chaitaly', 'score': 88, 'age': 20}, {'name': 'moni', 'score': 90, 'age': 19}, {'name': 'monisha', 'score': 95, 'age': 18}]


p=sorted(std,key=lambda d:d['score'], reverse=True)
print(p)    #o/p:[{'name': 'monisha', 'score': 95, 'age': 18}, {'name': 'moni', 'score': 90, 'age': 19}, {'name': 'chaitaly', 'score': 88, 'age': 20}]


