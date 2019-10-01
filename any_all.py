#any and all function

            ########## ALL FUNCTION ############
           # ---------------------------------------

n1=[2,4,6,8,10]
n2=[1,2,3,4,5,6,11,12]

for i in n1:
    if i%2==0:
        print(i)
        i+=1    #o/p:2
                    #4
                    #6
                    #8
                    #10
        
###another method  
even1=[]
even2=[]

for j in n1:
    even1.append(j%2==0)
print(even1) #o/p:[True, True, True, True, True]

for j in n2:
    even2.append(j%2==0)
print(even2)    #o/p:[False, True, False, True, False, True, False, True]


print(all(even1))   #o/p:True
print(all([True, True, True, True, True]))  #o/p:True

print(all(even2))   #o/p:False
print(all([False, True, False, True, False, True])) #o/p:False
      

######## short cut ############
print(all([k%2==0 for k in n1]))     #o/p:True
print(all([k%2==0 for k in n2]))     #o/p:False



            ######## ANY FUNCTION #########
            #----------------------------------------


print(any(even1))   #o/p:True
print(any([True, True, True, True, True]))  #o/p:True

print(any(even2))   #o/p:True
print(any([False, True, False, True, False, True])) #o/p:True
      

######## short cut ############
print(any([k%2==0 for k in n1]))     #o/p:True
print(any([k%2==0 for k in n2]))     #o/p:True


n3=[1,3,5]
print(any([k%2==0 for k in n3]))    #o/p:False

