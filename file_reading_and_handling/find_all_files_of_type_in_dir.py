import os

#finds all pdf files in a directory

def listing(rootdir, filetype='pdf'):
    files=[] 
    for dirpath,_,filenames in os.walk(rootdir):
        for f in filenames:
            if f.endswith(filetype):
                files.append(os.path.abspath(os.path.join(dirpath, f)))
    return files


if __name__=="__main__":
    rootdir='/Users/Me/Dropbox/fellowship_proposals'
    print( listing(rootdir))
#files=[] 
#for dirpath,_,filenames in os.walk(rootdir):
#    for f in filenames:
#        if f.endswith('pdf'):
#            files.append(os.path.abspath(os.path.join(dirpath, f)))
#
#print files
