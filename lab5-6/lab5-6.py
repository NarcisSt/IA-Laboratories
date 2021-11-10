import random


# Function to print the mastermind board
# def print_mastermind_board(passcode, guess_codes, guess_flags, k):
#     print("    |", end="")
#     for x in passcode:
#         print("\t" + x[:3], end="")
#     print()
#
#     for i in reversed(range(len(guess_codes))):
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print(guess_flags[i][0], guess_flags[i][1], "|")
#
#         print(guess_flags[i][2], guess_flags[i][3], end=" |")
#         for x in guess_codes[i]:
#             print("\t" + x[:3], end="")
#
#         print()
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print("Number of right colors: " + str(k))


def generate_random_code(colorsArray, n):
    random.shuffle(colorsArray)
    return colors[:n]


def compareCodes(passcode1, dummy_passcode1, code1, colors_map1):
    k = 0
    for x in code:
        if colors_map1[x] in dummy_passcode1:
            if code1.index(x) == passcode1.index(colors_map[x]):
                k += 1
    return k


# The Main function
if __name__ == '__main__':

    while True:
        try:
            code_length = int(input("\nPlease enter the length of the code(2/4/6): "))
            if code_length == 2 or code_length == 4 or code_length == 6:
                break
            else:
                print("\tPlease enter a valid number!")
                continue
        except ValueError:
            print("\tPlease enter a valid number!")
            continue

    colors = ["RED", "BLUE", "YELLOW", "GREEN", "PINK", "ORANGE"]
    colors_map = {1: "RED", 2: "BLUE", 3: "YELLOW", 4: "GREEN", 5: "PINK", 6: "ORANGE"}
    print("\n1 - RED, 2 - BLUE, 3 - YELLOW, 4 - GREEN, 5 - PINK, 6 - ORANGE")

    passcode = generate_random_code(colors, code_length)

    chances = 2 * (code_length + 2)

    print("You have " + str(chances) + " chances!\n")

    if code_length == 2:
        guess_codes = [['-', '-'] for x in range(chances)]
        guess_flags = [['-', '-'] for x in range(chances)]
        show_passcode = ['UNK', 'UNK']
    elif code_length == 4:
        guess_codes = [['-', '-', '-', '-'] for x in range(chances)]
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']
    elif code_length == 6:
        guess_codes = [['-', '-', '-', '-', '-', '-'] for x in range(chances)]
        guess_flags = [['-', '-', '-', '-', '-', '-'] for x in range(chances)]
        show_passcode = ['UNK', 'UNK', 'UNK', 'UNK', 'UNK', 'UNK']

    turn = 0
    k = 0
    while turn < chances:

        #        print_mastermind_board(show_passcode, guess_codes, guess_flags, k)

        try:
            code = list(map(int, input("Enter the code : ").split()))
        except ValueError:
            print("\tPlease enter a valid code!")
            continue

        if len(code) != code_length:
            print("\tPlease enter a valid code!")
            continue

        flag = 0
        for x in code:
            if x > 6 or x < 1:
                flag = 1

        if flag == 1:
            print("\tPlease enter a valid code!")
            continue

        for i in range(code_length):
            guess_codes[turn][i] = colors_map[code[i]]

        dummy_passcode = [x for x in passcode]

        pos = 0

        k = compareCodes(passcode, dummy_passcode, code, colors_map)

        for x in code:
            print("\t" + colors_map[x][:3], end="")
            if colors_map[x] in dummy_passcode:
                pos += 1
                dummy_passcode.remove(colors_map[x])

        random.shuffle(guess_flags[turn])

        print("\nNumber of right colors: " + str(k))

        if guess_codes[turn] == passcode:
            #            print_mastermind_board(passcode, guess_codes, guess_flags, k)
            print("You win! :)")
            print("The passcode was: ")
            for x in passcode:
                print("\t" + x[:3], end="")
            break

        turn += 1
        print("Number of attempts remaining: " + str(chances - turn) + "\n")

if turn == chances:
    #    print_mastermind_board(passcode, guess_codes, guess_flags, k)
    print("Game over! :(")
    print("The passcode was: ")
    for x in passcode:
        print("\t" + x[:3], end="")
