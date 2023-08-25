from array import *
a = array('i' , [1,2,3,4,5,6])
b = a[0]
n = len(a)
for i in range(0 , n-1):
    a[i] = a[i+1]
a[n-1] = b
print(a)
    
    
