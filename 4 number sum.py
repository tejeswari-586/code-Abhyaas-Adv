import numpy as np
a = np.array([2,3,1,4,6,0,5])
a.sort()
n = len(a)
sum = 10
for p in range(n):
    val1 = a[p]
    t = p+1
    j = n-1
    for t in range(n):
        val = a[t]
        i = t + 1
        j = n-2   
        while(i < j):
            k = a[i] + a[j] + val + val1
            if(k < sum):
                i += 1
            elif(k > sum):
                 j -= 1
            elif(k == sum):
               ((a[i] , a[j] , a[t] , a[p]))
               i += 1
               j -= 1

