L = [ ]
L1 = [ ]
n = int(input("Enter number of elements : "))
for i in range(0 , n):
    L.append(int(input("enter an element:")))
print(L)
for k in L:
    L1.append((k , L.count(k)))
print(L1)
L.clear( )
for x in L1:
    if  x not in L:
        L.append(x)
print(L)
L1 = L
m = int(n/2)
s = 0
for  j in range(len(L1)):
    if(L1[j][1] >= m):
        s=1
        print(L1[j][0])
if (s == 0):
    print("No majority element")
