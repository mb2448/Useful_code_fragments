import time
from print_on_one_line_only import Printer

class Timer():
    """
    Time something like a for loop
    only argument is max_iterations
    """
    def __init__(self, imax):
        self.t0 = time.time()
        self.i  = 0
        self.imax = imax
    def timeleft(self):
        telapsed =time.time()-self.t0
        pctdone = 100.0*(self.i+1)/self.imax
        tleft = (1-pctdone/100)/(pctdone/100/telapsed)
        percentstr= (format(pctdone, '.2f')+
                       "% done.  ") 
        timestr   = (format(tleft, '.1f')+" seconds remaining")
        self.i = self.i+1
        return (percentstr+timestr)

if __name__ == "__main__":
    nmax = 1000000
    tt= Timer(nmax)
    for i in range(nmax):
        j=i**3
        Printer(tt.timeleft())
