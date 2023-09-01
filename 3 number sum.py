import numpy as np
a = np.array([2,3,1,4,6,0,5])
a.sort()
n = len(a)
sum = 10
for t in range(n):
    val = a[t]
    i = t + 1
    j = n-1   
    while(i < j):
        k = a[i] + a[j] + val 
        if(k < sum):
           i += 1
        elif(k > sum):
           j -= 1
        elif(k == sum):
            print((a[i] , a[j] , a[t]))
            i += 1
            j -= 1

