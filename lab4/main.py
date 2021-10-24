import time
from lab4.problem import Problem
from lab4.solvers import BacktrackingForwardCheck, BacktrackingForwardCheckingMRV, BacktrackingMinimumRemainingValues

regions = ["T", "WA", "NT", "SA", "Q", "NSW", "V"]
borders = [("T", "V"), ("WA", "NT"), ("WA", "SA"), ("NT", "WA"), ("NT", "Q"),
           ("NT", "SA"), ("SA", "WA"), ("SA", "NT"), ("SA", "Q"), ("SA", "NSW"),
           ("SA", "V"), ("Q", "NT"), ("Q", "SA"), ("Q", "NSW"), ("NSW", "Q"),
           ("NSW", "SA"), ("NSW", "V"), ("V", "SA"), ("V", "NSW"), ("V", "T")]
colors = ["red", "blue", "green", "yellow"]


def read_problem_from_file(name):
    f = open(name, 'r')
    content = f.read()
    return content


def check_border(variables, *args):
    zipped = list(zip(variables, args))
    return zipped[0][1] != zipped[1][1]


def solve(solver):
    problem = Problem(solver)
    problem.add_variables(regions, colors)
    for node in regions:
        borders_per_node = [borders[index] for (index, a_tuple) in enumerate(borders) if a_tuple[0] == node]
        if borders_per_node:
            for border in borders_per_node:
                problem.add_constraint(check_border, list(border))

    start_time = time.time()
    problem.get_solution()
    end_time = (time.time() - start_time)
    print(f"Solution with {solver.get_description()} took {end_time} sec and {solver.counter} checks")
    problem.plot_map(borders)


def FC():
    solve(BacktrackingForwardCheck(forwardcheck=True))


def MRV():
    solve(BacktrackingMinimumRemainingValues(forwardcheck=False))


def FC_MRV():
    solve(BacktrackingForwardCheckingMRV(forwardcheck=True))


if __name__ == '__main__':

    # https://github.com/IvanSobko/map-coloring-csp
    # https://ktiml.mff.cuni.cz/~bartak/constraints/propagation.html

    while True:
        print("\nStrategies:")
        print("\t(1) BKT for Forward checking")
        print("\t(2) BKT for Minimum remaining values")
        print("\t(3) BKT for Forward checking + Minimum remaining values")
        selection = int(input("Select the search strategy you would like to use: "))

        if selection == 1:
            FC()
        elif selection == 2:
            MRV()
        elif selection == 3:
            FC_MRV()
        else:
            print("Invalid selection")
