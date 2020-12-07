import matplotlib.pyplot as plt
import numpy as np
import time
import os
import astropy.io.fits as pf

def writeout(data, outputfile, header=None, comment = None):
    hdu = pf.PrimaryHDU(data, header = header)
    if comment is not None:
        hdu.header.set('COMMENT', comment)
    hdulist = pf.HDUList([hdu])
    hdulist.writeto(outputfile,clobber = True)
    hdulist.close()

def ds9(data):
    writeout(data, 'temp.fits')
    os.system('/Applications/SAOImage\ DS9.app/Contents/MacOS/ds9 temp.fits &')
    pass

if __name__ == "__main__":
    #interactive non-locking plotting
    plt.ion()
    for i in range(10):
        plt.plot(np.random.random(10), np.random.random(10))
        plt.draw()
        plt.pause(0.01)
        time.sleep(0.2)
        plt.clf()
    plt.close()
    plt.ioff()
    
    #plotting and opening a window
    plt.plot(np.random.random(10), np.random.random(10))
    plot_title = 'myplot.png'
    plt.savefig(plot_title, dpi = 300)
    os.system('open '+plot_title)

    print ("Another option is to save your data as a fits file and then execute "+
           "a command to open the file with ds9.  This is very useful for image data.")
    print ("Starter code to do that is above; you would execute ds9(my2dimagedata)")

