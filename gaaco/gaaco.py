import random
import sys
import time
import copy
import math

#popsize = 100
EVAPORATION_RATE = 0.25
#MAX_F = 0.9
#MIN_F = 0.1
K_FACTOR = 0.80
Q_FACTOR = 1

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

def debug_phermone(g, population):
    file = open("debug_phermone.output", 'w')
    file.write("len of population is " + str(len(population)) + "\n")
    file.write("len of solution is " + str(len(population[0])) + "\n")
    for i in range(0, len(population)):
        file.write(str(i) + ":")
        for j in range(0, len(population[i]) - 1):
            _f = g[population[i][j]][population[i][j + 1]]['f']
            f = "{:.2f}".format(_f)
            file.write(f + " ")
        file.write("\n\n")
    
    
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
        return "{\n\tCost : " + "{0:.2f}".format(self.cost) + ",\n\tLength : " + str(len(self.solution)) + "\n\tData : " + str(self.solution) + "\n}"
    def __len__(self):
        return len(self.solution)
    def __getitem__(self, i):
        return self.solution[i]
    def __setitem__(self, i, v):
        self.solution[i] = v

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
    for i in range(1, len(g)):
        p = random.randint(0,len(data) - 1)
        solution[i] = data.pop(p)
    return Solution(solution, g)

def nearest_neighbor(g):
    """
    Generate Random Solution
    Always first element is 0 and Last element is (len(g) - 1)
    """
    solution = [None] * len(g)
    solution[0] = 0
    data = list(range(1, len(g)))
    for i in range(1, len(g)):
        p = None
        max_d = sys.maxsize
        for j in range(0, len(g)):
            if i != j and g[i][j]['d'] < max_d and j in data:
                max_d = g[i][j]['d']
                p = j
        solution[i] = p
        data.remove(p)
    return Solution(solution, g)

def populate(g, popsize):
    """
    Populate first generation with random data
    f for edge means phermone
    :return:
    """
    npopulation = list()
    for i in range(0, len(g)):
        for j in range(i + 1, len(g)):
            g[i][j]['f'] = 0.5
    npopulation.append(nearest_neighbor(g))
    for i in range(1, popsize):
        npopulation.append(generate_solution(g))
    npopulation.sort()
    return update_phermone(g, npopulation, popsize)

def update_phermone(g, population, popsize):
    #for i in population:
    #    print(i)
    #    i - len
    #   ----------
    #      len
    #

    for i in range(0, popsize):
        for j in range(0, len(population[i].solution) - 1):
            g[population[i].solution[j]][population[i].solution[j + 1]]['f'] +=  1 / (i + 1)
        g[population[i].solution[0]][population[i].solution[len(g) - 1]]['f'] +=  1 / (i + 1)

    #print("debuging")
    #for j in range(0, len(population[0].solution) - 1):
    #    g[population[0].solution[j]][population[0].solution[j + 1]]['f'] = 0.99 * (MAX_F - MIN_F)
    #    g[population[0].solution[0]][population[0].solution[len(g) - 1]]['f'] = 0.99 * (MAX_F - MIN_F)
    if __debug__:
        debug_population(population)
        debug_graph(g)
    return population

def solve(g, population, repeat=False):
    """
    Execute Genetic-Ant Algorithm on matrix
    :param matrix:
    :return:
    """
    if __debug__:
        print("solve function")
    while True:
        for i in range(0, 5):
            print(str(i) + " C1 " + "{0:.2f}".format(population[0].cost) + " C2 " + "{0:.2f}".format(population[1].cost) + " C3 " +"{0:.2f}".format(population[2].cost))
            ant(g, population)
            print(str(i) + " C1 " + "{0:.2f}".format(population[0].cost) + " C2 " + "{0:.2f}".format(population[1].cost) + " C3 " +"{0:.2f}".format(population[2].cost))
            population = genetic(g, population)
            print(str(i) + " C1 " + "{0:.2f}".format(population[0].cost) + " C2 " + "{0:.2f}".format(population[1].cost) + " C3 " +"{0:.2f}".format(population[2].cost))
        if not repeat:
            break

    return population[0].solution

def evaporate(g):
    if __debug__:
        print("evaporate")
    for i in range(0, len(g)):
        for j in range(i + 1, len(g)):
            g[i][j]['f'] =  g[i][j]['f'] * (1.0 - EVAPORATION_RATE)

class Edge():
    def __init__(self, i, f):
        self.i = i
        self.f = f
    def __lt__(self, other):
        return self.f < other.f
    def __le__(self, other):
        return self.f <= other.f
    def __eq__(self, other):
        return self.f == other.f
    def __gt__(self, other):
        return self.f > other.f
    def __ge__(self, other):
        return self.f >= other.f
    def __str__(self):
        return "{\n\tPhermone : " + "{0:.2f}".format(self.f) + ",\n\tEdge : " + str(self.i) + "\n}"
        

def ant_decision(g, solution, index):
    #print("ant_decision")
    #print(solution)
    l = list()
    all_p = 0.0
    for i in range(0, len(solution)):
        if i not in solution[0:index]:
            #print("index : " + str(index) + " i " + str(i))
            all_p += g[solution[index - 1]][i]['f']
            e = Edge(i, g[solution[index - 1]][i]['f'])
            l.append(e)
    l.sort(reverse=True)
    if all_p == 0:
        for i in l:
            print(i)
        sys.exit()
    def decision(probability):
        return random.random() < probability
    for i in l:
        if decision(i.f / all_p):
            return i.i
        else:
            all_p -= i.f
    print("Wrong Data Return. Fatal Error")
    sys.exit()
    
    
def ant(g, population):
    """
    First Every ant is in index 0,
    Then create a list of homes choosable from here range(1,len(g))
    until you filled the travel repeat :
        Then from available choice , pick up one of them based on roulette wheel
        (carefull , you should sort them based of their phermone)
    evaluate the route based on length
    sort the population
    return the population
    """
    if __debug__:
        print("ant function")

    for i in range(int(len(population)/20) + 1, len(population)):
        # For every ant
        for j in range(1, len(population[i]) - 1):
            # For every ant's node
            population[i][j + 1] = ant_decision(g, population[i], j + 1)
        population[i].evaluate(g)
    population.sort()
    evaporate(g)
    update_phermone(g, population, len(population))

def parent(population, ignore=None):
    wheel = 0.0
    all_cost = 0.0
    for i in range(0, len(population)):
        all_cost = population[i].cost
    for i in range(0, len(population)):
        if i != ignore:
            wheel += population[i].cost / all_cost
    #print("wheel is "+ str(wheel))
    r = random.uniform(0, wheel)
    #print("r is " + str(r))
    wheel = 0.0
    for i in range(0, len(population)):
        if i != ignore:
            wheel += population[i].cost / all_cost
            if wheel >= r:
                #print(i)
                return i
    # copy.deepcopy(population[i].solution)

def genetic(g, population):
    if __debug__:
        print("genetic function")
    p = list()
    for index in range(0, len(population)):
        child = list()
        parent_1_index = parent(population)
        parent_2_index = parent(population, parent_1_index)
        parent_1 = copy.deepcopy(population[parent_1_index].solution)
        parent_2 = copy.deepcopy(population[parent_2_index].solution)
        while len(parent_1) != 0:
            #print("parent_1 : " + str(parent_1))
            #print("parent_2 : " + str(parent_2))
            #print("child : " + str(child))
            new_len = math.ceil(K_FACTOR * len(parent_1))
            for i in range(0, new_len):
                child.append(parent_1.pop(0))
            for i in range(0, len(child)):
                if child[i] in parent_2:
                    parent_2.remove(child[i])
            parent_1, parent_2 = parent_2, parent_1
            #if __debug__:
        p.append(Solution(child, g))
    p.sort()
    #print("p best cost " + str(p[0].cost))
    p_index = 0
    population_index = 0
    new_population = list()
    keep = int(len(population) / 20) + 1
    for i in range(0, keep):
        new_population.append(population[population_index])
        population_index += 1
    for i in range(keep, len(population)):
        if population[population_index].cost < p[p_index].cost:
            new_population.append(population[population_index])
            population_index += 1
        else:
            new_population.append(p[p_index])
            p_index += 1
    new_population.sort()
    return new_population
