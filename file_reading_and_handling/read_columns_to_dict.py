import numpy as np
import pprint
import ipdb

def dictfromfile(filename, **kwargs):
    lines= np.genfromtxt(filename, **kwargs)

    dicty = {}
    for i in range(len(lines[0,:])):
        try:
            dicty[str(lines[0,i]).strip(" ")]=np.array(
                lines[1:, i], dtype=float)
        except:
            dicty[str(lines[0,i]).strip(" ")]=np.array(
                lines[1:, i], dtype=str)
    return dicty

if __name__ == "__main__":
    """Usage: dict = dictfromfile("myfile.txt", delim=" ")"""
    filename = 'filelist.txt'
    dicty = dictfromfile(filename, delimiter=',', dtype='str')
    pprint.pprint(dicty)
