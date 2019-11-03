#Enumerate Function

#we use enumerate function with for loop to track position of our item in variable

##############################
                       # print like this 0------> abc
                       #1------> abcdef
                       #2------> xyz
        ####normal
names=['abc','abcdef','xyz']
pos=0
for name in names:
    print(f"{pos}------> {name}")
    pos+=1

##### enumerate

info=['abc','abcdef','xyz']
for pos, name in enumerate(names):
    print(f"{pos}------> {name}")

