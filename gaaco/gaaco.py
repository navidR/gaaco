import random

popsize = 100
population = 0

class Solution():
    def __init__(self, solution, g):
        self.solution = solution
        self.evaluate(g)
    def evaluate(self, g):
        cost = 0
        for i in range(0, len(self.solution) - 1):
            cost += g[self.solution[i]][self.solution[i + 1]]['d']
        cost += g[self.solution[0]][self.solution[len(g) - 1]]['d']
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    def __eq__(self, other):
        return self.cost == other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __ge__(self, other):
        return self.cost >= other.cost
    def __str__(self):
        return str(self.cost) + " \n" + str(self.solution) + "\n"

def test_generate_solution(l):
    """
    Test Generated Data in Genearete Solution function
    """
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if i == j:
                continue
            elif l[i] == l[j]:
                print("generated data is wrong (" + str(i) + ", " + str(j) + ")")
                print(l)
                import sys
                sys.exit()
    return

def generate_solution(g):
    """
    Generate Random Solution
    Always first element is 0 and Last element is (len(g) - 1)
    """
    solution = [None] * len(g)
    solution[0] = 0
    solution[len(g) - 1] = len(g) - 1
    data = list(range(1, len(g) - 1))
    for i in range(1,len(g) - 1):
        solution[i] = data.pop(random.randint(0,len(data) - 1))
    s = Solution(solution, g)
    return s

def populate(g):
    """
    Populate first generation with random data
    :return:
    """
    global population
    population = list()
    for i in range(0, len(g)):
        for j in range(i + 1, len(g)):
            g[i][j]['f'] = 0
    for i in range(0, popsize):
        population.append(generate_solution(g))
    population.sort()
    return population

def solve(g):
    """
    Execute Gennetic-Ant Algorithm on matrix
    :param matrix:
    :return:
    """
    if __debug__:
        print("solve function")
    #print(population[0].cost)
    #print(population[0].solution)
    #populate(g)
    print("best Solution cost :" + str(population[0].cost))
    return population[0].solution
