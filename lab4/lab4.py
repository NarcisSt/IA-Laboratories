import sys
import queue

class Region:
    def __init__(self, region, region_neighbors, available_colors):
        self.region = region
        self.neighbors = region_neighbors
        self.colors = available_colors

    def get_arcs(self):
        arcs = []
        for i in range(len(self.neighbors)):
            arcs.append((self.region, self.neighbors[i]))
        return arcs


class Problem:
    def __init__(self, regions):
        self.regions = regions


def read_problem_from_file(name):
    f = open(name, 'r')
    content = f.read()
    return content


def FC(problem):
    solve(problem)


def MRV(problem):
    solve(problem)


def revise(problem, indexes, region_1, region_2):
    revised = False
    deleted = []
    for x in problem.regions[indexes[region_1]].colors:
        found = False
        for y in problem.regions[indexes[region_2]].colors:
            if x != y:
                found = True
                break
        if not found:
            revised = True
            deleted.append(x)
    for x in deleted:
        problem.regions[indexes[region_1]].colors.remove(x)
    return revised


def solve(problem):
    indexes = {}
    for i in range(len(problem.regions)):
        indexes[problem.regions[i].region] = i

    q = queue.Queue()
    for region in problem.regions:
        arcs = region.get_arcs()
        for arc in arcs:
            q.put(arc)

    solution_exists = True
    while not q.empty():
        el = q.get()
        region_1 = el[0]
        region_2 = el[1]
        index_1 = indexes[region_1]
        if revise(problem, indexes, region_1, region_2):
            if len(problem.regions[index_1].colors) == 0:
                solution_exists = False
            for x in problem.regions[index_1].neighbors:
                if x != region_2:
                    q.put((x, region_1))
        if not solution_exists:
            break

    print('---------------------------------')
    if solution_exists:
        for region in problem.regions:
            print("{}: {}".format(region.region, region.colors[0]))
    else:
        print("There is no solution!")


if __name__ == '__main__':
    pb1 = Problem(
        [
            Region("WA", ["SA", "NT"], ["R", "G", "B"]),
            Region("SA", ["WA", "NT"], ["R", "G"]),
            Region("NT", ["WA", "SA"], ["G"])
        ]
    )

    pb2 = Problem(
        [
            Region("T", ["V"], ["R", "B", "G"]),
            Region("WA", ["NT", "SA"], ["R"]),
            Region("NT", ["WA", "Q", "SA"], ["R", "B", "G"]),
            Region("SA", ["WA", "NT", "Q", "NSW", "V"], ["R", "B", "G"]),
            Region("Q", ["NT", "SA", "NSW"], ["G"]),
            Region("NSW", ["Q", "SA", "V"], ["R", "B", "G"]),
            Region("V", ["SA", "NSW", "T"], ["R", "B", "G"])
        ]
    )

    # pb1 = read_problem_from_file("pb1.txt")
    # pb2 = read_problem_from_file("pb1.txt")

    while True:
        print("\nStrategies:")
        print("\t(1) Forward checking")
        print("\t(2) Minimum remaining values")
        selection = int(input("Select the search strategy you would like to use: "))

        if selection == 1:
            FC(pb1)
        elif selection == 2:
            MRV(pb2)
        else:
            print("Invalid selection")
