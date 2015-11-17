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


def ijtoi(i, j):
    """
    Turn i,j to index for using with matrix
    :param i:
    :param j:
    :return:
    """
    return int(((i * (i - 1)) / 2) + j)


def init(point_list):
    """
    Calculate matrix of distance
    :return:matrix
    """
    l = len(point_list)
    matrix = (int((l * (l - 1)) / 2) * [None])
    for i in range(0, l):
        for j in range(0, i):
            # print("i is " + str(i) + " j is " + str(j) + " ijtoi is " + str(ijtoi(i, j)))
            matrix[ijtoi(i, j)] = euc_2d(point_list[i], point_list[j])
    if __debug__:
        print("matrix data:")
        print(matrix)
    return matrix

