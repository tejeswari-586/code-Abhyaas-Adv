import numpy as np
a = np.array([1, 1, 2, 2, 2, 5, 6, 3])
i = 0
j = 1
while(j < len(a)):
    if (a[i] == a[j]):
        j += 1
    else:
        i += 1
        a[i] = a[j]
k=0
while(k < i+1):
    print(a[k])
    k+=1
