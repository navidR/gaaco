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
POPSIZE = 50
INTERVAL = 2000
FACTOR = 1.0 # Ant and Genetic
EVAPORATION = 0.5
population = None

#if not __debug__:
parser = argparse.ArgumentParser()
parser.add_argument("-df", "--dataset-file", help="dataset which will be solved", required=True, type=str)
parser.add_argument("-dsf", "--dataset-solution-file", help="solution for dataset", type=str)
parser.add_argument("-v", "--verbose", help="increase output verbosity", default=False, type=bool)
parser.add_argument("-p", "--population-number", help="number of solution in your population", type=int, default=POPSIZE)
parser.add_argument("-pr", "--profile", help="printf profiler information", default=False,  action='store_true')
parser.add_argument("-i", "--interval", help="interval for drawing", type=int, default=INTERVAL)
parser.add_argument("-ag", "--atg", help="Ant-Genetic population size ratio", type=float, default=FACTOR)
parser.add_argument("-ng", "--no-gui", help="Without GUI", default=False, action='store_true')
args = parser.parse_args()

if args.dataset_solution_file is not None:
    file_solution_path = os.path.abspath(args.dataset_solution_file)
    ps_list = reader.reader.solution_reader(file_solution_path)
if args.profile is True:
    import cProfile
    pr = cProfile.Profile()
    pr.enable()

i = args.interval
file_path = os.path.abspath(args.dataset_file)
g = reader.reader.problem_reader(file_path)
if args.dataset_solution_file is not None:
    s = gaaco.gaaco.Solution(ps_list, g)
    print("best solution : cost " + str(s.cost))
    if __debug__:
        print("POPSIZE is " + str(POPSIZE))
        print("length : " + str(len(s.solution)))
        print("best solution object list :" + str(s.solution))
population = gaaco.gaaco.populate(g, POPSIZE)
if args.no_gui is False:
    plot.drawer.draw(g,  gaaco.gaaco.solve, population,ps_list=ps_list, i=i)
else:
    while True:
        gaaco.gaaco.solve(g, population, repeat=True)
if args.profile is True:
    pr.disable()
    pr.print_stats()
