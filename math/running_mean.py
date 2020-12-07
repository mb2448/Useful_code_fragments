
import numpy as np
array= np.random.random(100)

#main code here
i=0
mean = 0.0
for element in array:
    mean=mean*float(i)/(i+1) + element/float(i+1)
    print("N: ", i)
    print("running mean: ", mean)
    print("another way:  ", np.mean(array[0:i+1]))
    
    i=i+1   

