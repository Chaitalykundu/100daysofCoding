#zip function
                                            ########## PART 1 ##########
#it converts list to tuple inside list
user_id=['user1','user2','user3']
name=["moni","monisha","chaitaly"]
age=[19,20,21]

print(zip(user_id,name))    #o/p:<zip object at ###########>
      
print(list(zip(user_id,name)))  #o/p:[('user1', 'moni'), ('user2', 'monisha'), ('user3', 'chaitaly')]

#converting in dict:::
print(dict(zip(user_id,name)))  #o/p:{'user1': 'moni', 'user2': 'monisha', 'user3': 'chaitaly'}

#three items in tuple:
print(list(zip(user_id,name,age)))  #o/p:[('user1', 'moni', 19), ('user2', 'monisha', 20), ('user3', 'chaitaly', 21)]



##if there is a tuple and tuple has 2 items, then it can be converted into dict
##convert in dict::
ex=[("a",1),("b",2)]
print(dict(ex)) #o/p:{'a': 1, 'b': 2}

#print(dict(zip(user_id,name,age)))  #o/p:error( dictionary update sequence element #0 has length 3; 2 is required)


                                            ######## PART 2 ########
l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=list(zip(*l))
new=[]

print(l1)   #o/p:(1, 3, 5, 7)
print(l2)   #o/p:(2, 4, 6, 8)
print(list(l1)) #o/p:[1, 3, 5, 7]
print(list(l2)) #o/p:[2, 4, 6, 8]

for pair in zip(l1,l2):
    new.append(max(pair))
print(new)  #o/p:[2, 4, 6, 8] (because max nmb are in l2)
