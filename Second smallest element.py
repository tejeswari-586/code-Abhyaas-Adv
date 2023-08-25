import numpy as np
a = np.array([1, 5, 2, 3, 7, 6])
se  = 9999999999
sse = 9999999999
for j in range(0 , len(a)):
    if(a[j] < se):
        sse = se
        se = a[j]
    if(a[j]  < sse  and   a[j] != se):
        sse = a[j]
print("Second smallest  element:" , sse)
