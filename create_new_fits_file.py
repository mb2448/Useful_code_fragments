import numpy as np
import pyfits as pf

imagedata=np.zeros((100, 100), dtype = np.int32)

hdu = pf.PrimaryHDU(imagedata)
hdu.writeto('newfile.fits')
