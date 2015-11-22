# /bin/python3

import matplotlib
#matplotlib.use("GTK3Cairo")
matplotlib.use('GTK3Agg')

from . import drawer

if __debug__:
    print("Importing drawer module")
