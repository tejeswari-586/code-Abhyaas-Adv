from array import *
a = array('i' , [1 , 1 , 2 , 3 , 2 , 4 , 3 ])
s = 0
for i in range (0 , len(a)):
    s ^= a[i]
print(s)

