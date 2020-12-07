#Easiest numpy way
#returns an array
#see
#http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array


import numpy as np

filename = 'filelist.txt'
delim = ','
lines= np.genfromtxt(filename, dtype=str, delimiter=delim, skip_header=1)

print(lines)

print(" ")
print("first column, ", lines[:,0])
print("first row, ", lines[0,:])
