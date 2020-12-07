import astropy.io.fits as pf
#see http://www.astropython.org/tutorial/2010/10/PyFITS-FITS-files-in-Python

fitsfile='test.fit'
print( pf.info(fitsfile))

data, header = pf.getdata(fitsfile, 0, header=True, memmap=True)
print(header)
#print(data)

