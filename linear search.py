a = [1,2,3,4,5,6,7,8,9]
x = int(input("enter the element to search: "))
s = 0
for i in range(0 , len(a)):
    if (a[i] == x):
        s = 1
        break
if (s ==1):
    print("The element is found at the index : " , i)
else :
    print("The element is not found") 
