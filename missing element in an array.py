from array import *
a = array('i' , [10 , 20 , 30 , 32 , 45 , 52])
sub = array('i' ,[10 , 20 , 32 , 45 , 52])
sum = 0
for i in range(0 , len(a)):
    sum = sum + a[i]
for j in range(0 , len(sub)):
    sum = sum - sub[j]

print(sum)
 
