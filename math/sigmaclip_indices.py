import numpy as np

arr=np.random.normal(0, 1, 10000).reshape((100, 100))

siglvl=3

mean=np.mean(arr)
std =np.std(arr)
goodmask=np.where( (arr > (mean - siglvl*std)) |
                   (arr < (mean + siglvl*std)))

badmask =np.where( (arr < (mean - siglvl*std)) |
                   (arr >(mean + siglvl*std)))

badvalues = arr[badmask]
