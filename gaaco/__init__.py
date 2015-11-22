#!/bin/python3

if __debug__:
    print("importing gaaco")

from . import gaaco
import math

def euc_2d(startx_starty, endx_endy):
    """
    Calculate eucldean distance between (startx, starty),(endx, endy)
    :param startx_starty:(startx, starty)
    :param endx_endy:(endx, endy)
    :return:
    """
    startx, starty = startx_starty
    endx, endy = endx_endy
    return float(math.sqrt(pow(abs(startx - endx), 2) + pow(abs(starty - endy), 2)))


def init(g):
    """
    :g:networkx.Graph
    Calculate matrix of distance
    :return:networkx.Graph
    """
    



