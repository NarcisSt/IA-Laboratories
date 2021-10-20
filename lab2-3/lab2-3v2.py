from copy import deepcopy
import time
import sys


class State:
    shore = None  # array with the position of the people in the order w1, w2,... h1, h2, ... (0 for left shore, 1 for right shore)
    boat = 0  # position of the boat (0 for left shore, 1 for right shore)
    depth = 0  # equals path cost in this example because unit step cost = 1
    path = None  # array of States that lead to the current State

    def __init__(self, s=[], b=0):
        self.shore = s
        self.boat = b
        self.depth = 0
        self.path = []

    def f(self):  # evaluation function
        return self.depth + h(self)


def jealousy(current):
    for i in range(0, couples):
        if current.shore[i] != current.shore[couples + i]:  # husband is not with his wife
            for j in range(couples, couples * 2):
                if (current.shore[j] == current.shore[i]):  # another man is with the wife
                    return 1
    return 0


def alterbit(bit):  # used to change position of people or the boat
    return abs(bit - 1)


def isGood(state):  # people on the same side as the boat are "good"
    good_people = deepcopy(state.shore)
    for i in range(0, len(state.shore)):
        if state.shore[i] == state.boat:
            good_people[i] = 1
    return good_people


def h(state):  # the heuristic function equals the number of people who are not on the goal shore
    result = len(state.shore)
    for i in state.shore:
        result = result - i
    return result


def visited(state, searched):  # determines whether a State has already been visited
    for k in range(0, len(searched)):
        if state.shore == searched[k].shore and state.boat == searched[k].boat:
            return True
    return False


def move(cap, state, movement, result,
         start):  # computes all possible moves from a current State with a certain boat capacity
    for i in range(start, len(state.shore)):
        if isGood(state)[i] == 1:  # if the person is on the same side as the boat
            movement.append(i)  # add the person to the list of possible moves
            if cap > 1:  # if there is more space in the boat
                move(cap - 1, state, movement, result,
                     i)  # iterate; start for-loop with i to prevent duplicates (permutations)
            if cap == 1:  # if the boat is full
                result.append(deepcopy(movement))  # add move to the result array
            movement.pop()  # when returning to the outer iteration, pop the last item
    return result  # return an array of possible moves


def expand(state):
    result = []
    possible_moves = move(capacity, state, [], result,
                          0)  # get all possible moves for the current State and capacity
    for i in possible_moves:  # iterate through all possible state changes
        following = deepcopy(state)
        for j in i:
            following.shore[j] = alterbit(state.shore[j])  # move persons
        following.boat = alterbit(state.boat)  # move boat
        if visited(following, searched):  # check if state was already visited
            True
        elif jealousy(following):  # check if there is it's not ok
            searched.append(following)
        elif True:
            following.depth = following.depth + 1  # increase depth
            following.path.append(state)  # add the parent node to the path
            frontier.append(following)  # add the node to the frontier


def BFS():
    statesNumber = 0
    d = -1  # current depth
    while True:
        statesNumber = statesNumber + 1
        print("Visited states: ", statesNumber)

        current = frontier.pop(0)  # examine first item from frontier (FIFO)

        if h(current) == 0:  # goal check
            return current  # if heuristic function equals 0, the goal is reached
        if current.depth != d:  # print depth if changed
            d = current.depth
            print("current depth: ", d)

        expand(current)  # expand and add new states to frontier
        searched.append(current)  # add the current node to the closed list


def BKT():
    statesNumber = 0
    while True:
        statesNumber = statesNumber + 1
        print("Visited states: ", statesNumber)

        current = frontier.pop()  # examine last item from frontier (LIFO)

        if h(current) == 0:  # goal check
            return current  # if heuristic function equals 0, the goal is reached

        expand(current)  # expand and add new states to frontier
        searched.append(current)


def HILL():
    print("Not implemented yet")


def ASTAR():
    statesNumber = 0
    while True:
        statesNumber = statesNumber + 1
        print("Visited states: ", statesNumber)

        frontier.sort(key=lambda state: state.f())  # sort frontier according to evaluation function

        current = frontier.pop(0)  # examine first item of the frontier (item with the lowest evaluation function)

        if h(current) == 0:  # goal check
            return current  # if heuristic function equals 0, the goal is reached

        expand(current)  # expand and add new states to frontier
        searched.append(current)  # add the current node to the closed list


if __name__ == '__main__':
    couples = int(input("Enter the number of couples: "))
    capacity = int(input("How many persons can the boat hold: "))

    time.perf_counter()

    couple = [0, 0]
    initial = State([], 0)
    goal = State([], 0)
    path = []
    frontier = []  # open list (frontier)
    searched = []  # closed list
    statesNumber = 0

    for i in range(0, couples):  # add couples on left side of the river
        initial.shore.extend(
            couple)  # the state will be treated as wife1, wife2, wife3, ... husband1, husband2, husband3, ...

    frontier.append(initial)  # add initial node to frontier

    print("\nStrategies:")
    print("\t(1) Backtracking")
    print("\t(2) Breadth-First-Search")
    print("\t(3) Hillclimbing")
    print("\t(4) A*-Search-Algorithm")
    selection = int(input("Select the search strategy you would like to use: "))

    if selection == 1:
        goal = BKT()  # search with BKT, implemented
    elif selection == 2:
        goal = BFS()  # search with BFS, implemented
    elif selection == 3:
        HILL()
    elif selection == 4:
        goal = ASTAR()  # search with A*, implemented
    else:
        print("Invalid selection")
        sys.exit()

    print("\nSuccess: ", goal.shore, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.shore)
    print("Path: ", path)
