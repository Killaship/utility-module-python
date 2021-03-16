

"""

UTILITIES MODULE

==============================
|Some degree of documentation|
==============================

Current functions:
loadingbar(how many marks in the loading bar , delay between the marks (defaults to 0.3) [optional param] , character to use (defaults to #) [optional param])


"""


def loadingbar(x,y=0.3,z="#"):
 import time
 print("\n")
 for _ in range(x):
     time.sleep(y)
     print(z, end="",flush=True)
 print("\n")
 print("Done loading")
 print("\n")

def test():
    return 'hello world'

    





