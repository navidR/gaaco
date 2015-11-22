#!/bin/python3

import argparse
import plot
import reader
import gaaco
import os

DATASET_FILE = None
DATASET_SOLUTION_FILE = None
args = None
points_solution_list = None
X = 'x'
Y = 'y'
DISTANCE = 'd'

#if not __debug__:
parser = argparse.ArgumentParser()
parser.add_argument("-df", "--dataset-file", help="dataset which will be solved", required=True)
parser.add_argument("-dsf", "--dataset-solution-file", help="solution for dataset")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

if args.dataset_solution_file is not None:
    file_solution_path = os.path.abspath(args.dataset_solution_file)
    ps_list = reader.reader.solution_reader(file_solution_path)

file_path = os.path.abspath(args.dataset_file)
g = reader.reader.problem_reader(file_path)
if args.dataset_solution_file is not None:
    s = gaaco.gaaco.Solution(ps_list, g)
    print("best solution : cost " + str(s.cost))
    if __debug__:
        print("length : " + str(len(s.solution)))
        print("best solution object list :" + str(s.solution))
gaaco.gaaco.populate(g)
plot.drawer.draw(g, ps_list, gaaco.gaaco.solve)
