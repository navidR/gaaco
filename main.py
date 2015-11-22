#!/bin/python3

DATASET_FILE = None
DATASET_SOLUTION_FILE = None
args = None
points_solution_list = None
X = 'x'
Y = 'y'
DISTANCE = 'd'


import argparse
import plot
import reader
import gaaco
import os


#if not __debug__:
parser = argparse.ArgumentParser()
parser.add_argument("-df", "--dataset-file", help="dataset which will be solved", required=True)
parser.add_argument("-dsf", "--dataset-solution-file", help="solution for dataset")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
DATASET_FILE = args.dataset_file
DATASET_SOLUTION_FILE = args.dataset_solution_file
#else:
#    print("Use Debug Config")
#    DATASET_FILE = "./datasets/att48.tsp"
#    DATASET_SOLUTION_FILE = "./datasets/att48.opt.tour"

#if __debug__:
#    print("verbosity turned on")

if DATASET_SOLUTION_FILE is not None:
    file_solution_path = os.path.abspath(DATASET_SOLUTION_FILE)
    points_solution_list = reader.reader.solution_reader(file_solution_path)

file_path = os.path.abspath(DATASET_FILE)
points_list = reader.reader.problem_reader(file_path)
#matrix = gaaco.init(points_list)
#plot.drawer.draw(points_list, points_solution_list, gaaco.gaaco.solve, matrix)
