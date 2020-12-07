import numpy as np

A=np.arange(100)
B=np.random.random(100)
with open('output2col.txt', 'w') as f:
    for f1, f2 in zip(A, B):
        print(f1, f2, file=f)
        #python 3
        #print(f2, f2, file=f)
