from array import *
a = array('i' , [5, 5, 4, 3, 2, 1])
n = len(a)
s = 1
j = 0
while(a[j] == a[j+1] and  j+1 < n):
    j += 1
if(a[j] > a[j+1]):
    for i in range(1 , n):
        if(i+1 < n  and a[i] < a[i+1]):
            s = 0
            break
elif(a[j] < a[j+1]):
    for i in range(1 , n):
        if(i+1 < n  and  a[i] > a[i+1]):
            s = 0
            break
if  s == 1:
    print("Array is sorted")
else:
    print("Array is not sorted")
