import numpy as np
a = np.array([1, 5, 2, 3, 7, 6])
le =  -999999999
sle = -999999999
for i in range(0 , len(a)):
        if(a[i] > le):
                sle = le
                le = a[i]
if(a[i] > sle  and   a[i] != le):
             sle = a[i]
print("Second largest element:" , sle)



             
