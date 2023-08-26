from array import *
a = array('i' , [1,2,3,4,5,6,7])
x = int(input("enter the element to search: "))
n = len(a)
low = 0
high = n-1
mid =int( (low + high)/2)
while(low < high  and  a[mid] != x):
    if (a[mid] < x):
        low = mid + 1
    elif(a[mid] > x):
        high = mid - 1
    mid = int((high + low)/2)

if(a[mid] == x):
    print("The element is found at the index :" , mid)
else :
    print("Element not found")

              

          
