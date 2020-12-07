import ipdb
def myfunc(mainargument, x=None, *args, **kwargs):
    if x is not None:
        print "x was passed"

    if 'y' in locals().copy()['kwargs']:
        print "y was passed as an optional keyword"
    x=4
    return mainargument

if __name__ == "__main__":
    codestring1='myfunc(3,6, y= 4)'
    print codestring1
    eval(codestring1)
    codestring2='myfunc(2)'
    print codestring2
    eval(codestring2)
    codestring3='myfunc(3, 6,  z=10)'
    print codestring3
    eval(codestring3)
