import astropy.io.fits as pf
import numpy as np
import os

def ds9(a):
    pf.writeto('temp.fits', np.array(a), overwrite=True)
    os.system('ds9 temp.fits -zoom to fit &')
    return

if __name__ == "__main__":
    ds9(np.random.random((10, 10))) 
