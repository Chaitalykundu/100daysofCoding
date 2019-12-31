#list vs generator


#space calculate:::
#list
square=[i**2 for i in range(1,11)]
print(square)


#generator 
square=(i**2 for i in range(1,11))
print(square)

#    N.B.--- list needs more space than generator



#time calculate:::

import time

t1=time.time()
l=[i**2 for i in range(1000000)]
print(time.time() - t1)     #o/p:1.4687747955322266


t2=time.time()
g=(i**2 for i in range(1000000))
print(time.time() - t2)     #O/P:0.0

