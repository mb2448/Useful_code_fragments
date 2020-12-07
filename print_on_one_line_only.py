from sys import stdout
from time import sleep
import sys
 
class Printer():
    """
    Print things to stdout on one line dynamically
    """
    def __init__(self,data):
 
        sys.stdout.write("\r\x1b[K"+data.__str__())
        sys.stdout.flush()
if __name__ == "__main__":
    listy=['a', 3, 'bb34', 'hi']

    print("Beginning")
    for item in listy:
        Printer(item)
        sleep(0.4)
