import random


class State:
    steps = 0
    n = 0
    m = 0
    k = 0

    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        self.steps = 0


def getInitialState(n, m, k):
    return State(n, m, k)


def isFinal(state):
    if state.steps > 2 * state.n:
        return True  # A a castigat
    else:
        return False  # B a castigat


def countFromArray(array, n):
    return array.count(n)


def selectRandom(state):
    numbers = random.randrange(1, state.m * state.n)
    lst1 = []
    for value in range(numbers):
        aux1 = random.randrange(state.n)
        first_tuple_elements = [a_tuple[0] for a_tuple in lst1]
        if countFromArray(first_tuple_elements, aux1) < state.m:
            lst2 = [aux1, random.randrange(1, state.m)]
            lst1.append(lst2)
        else:
            lst2 = [random.randrange(1, state.n), random.randrange(1, state.m)]
            lst1.append(lst2)
    return lst1


if __name__ == '__main__':
    initialState = getInitialState(4, 3, 2)
    print(selectRandom(initialState))
