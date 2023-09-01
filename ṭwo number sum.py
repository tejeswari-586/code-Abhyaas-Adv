import numpy as np
a = np.array([2,3,1,4,6,0,5])
a.sort()
n = len(a)
sum = 6
i = 0
j = n-1
while(i < j):
    k = a[i] + a[j]
    if(k < sum):
        i += 1
    elif(k > sum):
        j -= 1
    elif(k == sum):
        print((a[i] , a[j]))
        i += 1
        j -= 1

