import sys


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


def FC(problem):
    print("Not implemented yet")


def MRV(problem):
    print("Not implemented yet")


if __name__ == '__main__':
    pb = Problem(
        [
            Region("WA", ["SA", "NT"], ["R", "G", "B"]),
            Region("SA", ["WA", "NT"], ["R", "G"]),
            Region("NT", ["WA", "SA"], ["G"])
        ]
    )

    pb1 = Problem(
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

    print("\nStrategies:")
    print("\t(1) Forward checking")
    print("\t(2) Minimum remaining values")
    selection = int(input("Select the search strategy you would like to use: "))

    if selection == 1:
        FC(pb)
    elif selection == 2:
        MRV(pb1)
    else:
        print("Invalid selection")
        sys.exit()
