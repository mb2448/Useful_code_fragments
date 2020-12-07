import numpy as np
import sys
import ipdb

def round_sig(x, sig=2):
    if x ==0:
        return 0
    if x <0:
        minusx=-x
        return -1*round(minusx, sig-int(np.floor(np.log10(minusx)))-1)
    else:
        return round(x, sig-int(np.floor(np.log10(x)))-1)
if __name__ == "__main__":
    print "q to exit"
    while True:
        x=raw_input("Enter a number: ")
        n=raw_input("Enter sig fig: ")
        if x=='q' or n=='q':
            sys.exit(0)
        print round_sig(float(x),sig=int(n))
