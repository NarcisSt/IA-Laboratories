ACTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]
STATES = ["START", "BLANK", "ICE", "END"]
n = 9
m = 9
maze = [[2, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 3]]

D_LIN = [-1, 0, 1, 0]
D_COL = [0, 1, 0, -1]
VISITED_STATES = [[0 for _ in range(n)] for _ in range(n)]


def init_q_table(actions1, states1):
    q_table = [[0 for _ in range(len(actions1))] for _ in range(len(states1))]
    return q_table


def get_maze_position(cell_value):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == cell_value:
                return i, j
    return None


def not_visited(state):
    position = get_maze_position(state)
    lst = list(position)
    return VISITED_STATES[lst[0]][lst[1]]


def get_new_state(state, action):
    position = ()
    if not_visited(state) == 0:
        if state == 3 or state == 1:
            return "You are on ice or finish position"
        if state == 2 or state == 0:
            position = get_maze_position(state)
            if action == "UP":
                lst = list(position)
                lst[0] -= 1
                VISITED_STATES[lst[0]][lst[1]] = 1
                position = tuple(lst)
            elif action == "DOWN":
                lst = list(position)
                lst[0] += 1
                VISITED_STATES[lst[0]][lst[1]] = 1
                position = tuple(lst)
            elif action == "RIGHT":
                lst = list(position)
                lst[1] += 1
                VISITED_STATES[lst[0]][lst[1]] = 1
                position = tuple(lst)
            elif action == "LEFT":
                lst = list(position)
                lst[1] -= 1
                VISITED_STATES[lst[0]][lst[1]] = 1
                position = tuple(lst)
            else:
                return "Incorrect action"
            lst = list(position)
            if lst[0] < 0 or lst[1] < 0:
                return "Invalid action"
    else:
        print("State already visited")

    return position


class Maze:
    pass


if __name__ == '__main__':
    iterations_count = int(input("\nPlease enter the number of iterations: "))
    learning_rate = float(input("\nPlease enter the learning rate:"))
    next_prize = float(input("\nPlease enter the value of future reward"))
    print(init_q_table(ACTIONS, STATES))
    print(get_maze_position(2))
    print(get_new_state(2, "LEFT"))
