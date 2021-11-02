import random


# Function to print the mastermind board
def print_mastermind_board(passcode, guess_codes, guess_flags, k):

    print("    |", end="")
    for x in passcode:
        print("\t" + x[:3], end="")
    print()

    for i in reversed(range(len(guess_codes))):
        print("------------------------------")
        print(guess_flags[i][0], guess_flags[i][1], "|")

        print(guess_flags[i][2], guess_flags[i][3], end=" |")
        for x in guess_codes[i]:
            print("\t" + x[:3], end="")

        print()
    print("------------------------------")
    print("Number of right colors: " + str(k))


def generate_random_code(colorsArray):
    random.shuffle(colorsArray)
    return colors[:4]


def compareCodes(passcode1, dummy_passcode1, code1, colors_map1):
    k = 0
    for x in code:
        if colors_map1[x] in dummy_passcode1:
            if code1.index(x) == passcode1.index(colors_map[x]):
                k += 1
    return k


# The Main function
if __name__ == '__main__':

    colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "ORANGE"]
    colors_map = {1: "RED", 2: "GREEN", 3: "YELLOW", 4: "BLUE", 5: "BLACK", 6: "ORANGE"}

    passcode = generate_random_code(colors)

    chances = 8

    show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']

    guess_codes = [['-', '-', '-', '-'] for x in range(chances)]

    guess_flags = [['-', '-', '-', '-'] for x in range(chances)]

    turn = 0
    k = 0
    while turn < chances:

        print("\n\n1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE\n\n")
        print_mastermind_board(show_passcode, guess_codes, guess_flags, k)

        try:
            code = list(map(int, input("Enter the code : ").split()))
        except ValueError:
            print("\tPlease enter a valid code!")
            continue

        if len(code) != 4:
            print("\tPlease enter a valid code!")
            continue

        flag = 0
        for x in code:
            if x > 6 or x < 1:
                flag = 1

        if flag == 1:
            print("\tPlease enter a valid code!")
            continue

        for i in range(4):
            guess_codes[turn][i] = colors_map[code[i]]

        dummy_passcode = [x for x in passcode]

        pos = 0

        k = compareCodes(passcode, dummy_passcode, code, colors_map)

        for x in code:
            if colors_map[x] in dummy_passcode:
                if code.index(x) == passcode.index(colors_map[x]):
                    guess_flags[turn][pos] = 'K'
                pos += 1
                dummy_passcode.remove(colors_map[x])

        random.shuffle(guess_flags[turn])

        if guess_codes[turn] == passcode:
            print_mastermind_board(passcode, guess_codes, guess_flags, k)
            print("You win! :)")
            break

        turn += 1
        

if turn == chances:
    print_mastermind_board(passcode, guess_codes, guess_flags, k)
    print("Game over! :(")
