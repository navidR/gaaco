import random

#popsize = 100
EVAPORATION_RATE = 0.5
MAX_F = 0.9999
MIN_F = 0.0000

def debug_graph(g):
    file = open("debug_graph_nodes.output", 'w')
    file.write("len of node : " + str(len(g.node)) + "\n")
    for i in range(0, len(g)):
        file.write(str(i) + " : " + str(g.node[i]) + "\n")
    file.close()
    file = open("debug_graph_edges.output", 'w')
    file.write("len of edge : " + str(len(g.edges())) + "\n")
    for i in range(0, len(g.edge)):
        for j in range(0, len(g.edge)):
            if i != j:
                f = "{:.2f}".format(g[i][j]['f'])
                d = "{:.2f}".format(g[i][j]['d'])
                file.write("(" + str(i) + ","+ str(j) + ")" + ":d:" + d + ":f:" + f + ",")
        file.write("\n\n")
    file.write("\n")
    file.close()


def debug_population(population):
    file = open("debug_population.output", 'w')
    file.write("len of population is " + str(len(population)) + "\n")
    file.write("len of solution is " + str(len(population[0])) + "\n")
    for i in range(0, len(population)):
        file.write("c:" + str(int(population[i].cost)) + ":")
        for j in range(0, len(population[i])):
            file.write("{0:3}".format(population[i][j]))
        file.write("\n")
    

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
    def __len__(self):
        return len(self.solution)
    def __getitem__(self, i):
        return self.solution[i]

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
    data = list(range(1, len(g)))
    for i in range(1,len(g)):
        p = random.randint(0,len(data) - 1)
        solution[i] = data.pop(p)
    s = Solution(solution, g)
    return s

def populate(g, popsize):
    """
    Populate first generation with random data
    f for edge means phermone
    :return:
    """
    population = list()
    for i in range(0, len(g)):
        for j in range(i + 1, len(g)):
            g[i][j]['f'] = 0.0
    for i in range(0, popsize):
        population.append(generate_solution(g))
    population.sort()
    #for i in population:
    #    print(i)
    step = (MAX_F - MIN_F) / (popsize + 1)
    phermone = 0
    print("phermone " + str(phermone))
    print("step is " + str(step))
    for i in reversed(range(0, popsize)):
        for j in range(0, len(population[i].solution) - 1):
            g[population[i].solution[j]][population[i].solution[j + 1]]['f'] = phermone
        g[population[i].solution[0]][population[i].solution[len(g) - 1]]['f'] = phermone
        phermone += step
        if __debug__:
            print("phermone in next step " + str(phermone))
    if __debug__:
        debug_population(population)
        debug_graph(g)
    return population

def solve(g, population):
    """
    Execute Genetic-Ant Algorithm on matrix
    :param matrix:
    :return:
    """
    #population = None
    if __debug__:
        print("solve function")
    #print(population[0].cost)
    #print(population[0].solution)
    #population = populate(g, popsize)
    implement_algorithm(g, population)
    print("best Solution cost : " + str(population[0].cost))
    return population[0].solution

def implement_algorithm(g, population):
    if __debug__:
        print("Implement Algorithm")
    ant(g, population)
    genetic(g, population)

def evaporate(g):
    if __debug__:
        print("evaporate")
    for i in range(0, len(g)):
        for j in range(i + 1, len(g)):
            g[i][j]['f'] =  g[i][j]['f'] * (1 - EVAPORATION_RATE)

        
def ant(g, population):
    if __debug__:
        print("ant function")
    
        
    population.sort()

        
def genetic(g, population):
    if __debug__:
        print("genetic function")

    population.sort()


