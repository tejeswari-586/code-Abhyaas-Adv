from array import *
a = array('i' , [10, 12, 13, 14, 15])
s = int(input("enter no of shifts:"))
i = 0
k = i+s
b = [ ]
while(k < len(a)):
        b.append(a[k])
        k+=1
j = 0
k = len(b)
while(k < len(a)):
        b.append(a[j])
         j += 1
        k += 1
print(b)
          
