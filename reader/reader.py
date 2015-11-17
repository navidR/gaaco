#!/bin/python3

import traceback
import sys

COLON_CHAR = ":"
SPACE_CHAR = " "

NAME_STR = "NAME"
COMMENT_STR = "COMMENT"
TYPE_PROBLEM_STR = "TSP"
TYPE_SOLUTION_STR = "TOUR"
DIMENTION_STR = "DIMENTION"
EDGE_WEIGHT_TYPE_STR = "EDGE_WEIGHT_TYPE"
NODE_COORD_SECTION_STR = "NODE_COORD_SECTION"
EOF_STR = "EOF"
TOUR_SECTION_STR = "TOUR_SECTION"


def problem_reader(file_addr):
    """
    Read TSP data from file and Construct matrix of cost.

    file:
    Address of file
    """
    print("opening " + file_addr + " for reading TSP dataset")
    try:
        file = open(file_addr)
    except FileNotFoundError:
        print("Couldn't open : " + file_addr)
        traceback.print_exc()
        sys.exit()
    f_name = file.readline().split(COLON_CHAR)[1].strip()
    f_comment = file.readline().split(COLON_CHAR)[1].strip()
    f_type = file.readline().split(COLON_CHAR)[1].strip()

    # if f_type != TYPE_PROBLEM_STR:
    # print("TSP File Header is Wrong")
    # sys.exit()

    f_dimention = int(file.readline().split(COLON_CHAR)[1].strip())
    f_edge_type = file.readline().split(COLON_CHAR)[1].strip()

    print("detailed information:")
    print("file name : " + f_name)
    print("comment : " + f_comment)
    print("file type : " + f_type)
    print("file dimention : " + str(f_dimention))
    print("file edge type : " + f_edge_type)

    if NODE_COORD_SECTION_STR == file.readline().strip():
        point_list = [None] * f_dimention
        for i in range(f_dimention):
            line = file.readline()
            index, x, y = line.split(SPACE_CHAR)
            index.strip()
            x.strip()
            y.strip()
            point_list[i] = (int(x), int(y))
    if EOF_STR == file.readline().strip():
        print("dataset read was successfull")
    if __debug__:
        print("Datalist length : " + str(len(point_list)))
        print(point_list)
    return (point_list)


def solution_reader(file_addr):
    """
    Read TSP solution file and Return solution
    :return:
    """
    print("opening " + file_addr + " for reading TSP solution")
    try:
        file = open(file_addr)
    except FileNotFoundError:
        print("Couldn't open : " + file_addr)
        traceback.print_exc()
        sys.exit()
    f_name = file.readline().split(COLON_CHAR)[1].strip()
    f_comment = file.readline().split(COLON_CHAR)[1].strip()
    f_type = file.readline().split(COLON_CHAR)[1].strip()

    if f_type != TYPE_SOLUTION_STR:
        print("Tour File Header is Wrong")
        sys.exit()

    f_dimention = int(file.readline().split(COLON_CHAR)[1].strip())
    if TOUR_SECTION_STR == file.readline().strip():
        point_list = [None] * f_dimention
        for i in range(f_dimention):
            point = file.readline().strip()
            point_list[i] = int(point) - 1
    if __debug__:
        print("Solution length : " + str(len(point_list)))
        print(point_list)
    return point_list


if __name__ == "__main__":
    problem_reader(sys.argv[1])
