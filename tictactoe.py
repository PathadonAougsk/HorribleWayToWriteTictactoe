from ntpath import sep
def define_boardsize():
    while True:
        board_size = int(input("Enter board size n for n x n board (3-10): "))
        if board_size >= 3 or board_size <= 10:
            return board_size

        print("Out of the board range try again")

def define_usersymbol():
    temp_symbol = []
    text_holder = ""
    current_order = 1
    while True:
        user_symbol = input(f"Enter Player {current_order}'s symbol (a single letter{text_holder}): ")
        if len(user_symbol) > 1:
            print("Invalid Symbol length try again")
            continue

        if not user_symbol.isalpha() or user_symbol in temp_symbol:
            print("Invalid Symbol try again")
            continue

        temp_symbol.append(user_symbol)
        text_holder = f", different from '{user_symbol}'"
        current_order += 1

        if len(temp_symbol) >= 2:
            break
    return temp_symbol[0], temp_symbol[1]

def define_dict(board_size):
    temp_dict = {}
    for number in range(1, board_size ** 2 + 1):
        temp_dict[number] = number

    return temp_dict

def create_board(dict_board, size):
    seperator = 7

    if size == 3:
        seperator = 3

    print(("+" + "-" * seperator) * size , end="+\n")
    for number in range(1, len(dict_board) + 1):
        front_spacing, back_spacing, seperator = 3, 3, 7

        if size != 3:
            if not str(dict_board[number]).isnumeric():
                front_spacing = 3
                back_spacing = 3
            elif dict_board[number] > 9 and dict_board[number] <= 99 :
                front_spacing = 2
                back_spacing = 3
            elif dict_board[number] > 99:
                front_spacing = 2
                back_spacing = 2

        else:
            front_spacing = 1
            back_spacing = 1
            seperator = 3

        if number % size == 0:
            print(f"|{' ' * front_spacing}{dict_board[number]}{' ' * back_spacing}|")
            print(("+" + "-" * seperator) * size , end="+\n")
        else:
            print(f"|{' ' * front_spacing}{dict_board[number]}{' ' * back_spacing}", end="")

def user_decision(dict_board, player_symbol, board_size):
    text = "Player {playerSymbol}, enter your move postion (1-{boardSize}): "
    create_board(dict_board, board_size)
    while True:
        move_position = input(text.format(playerSymbol = player_symbol, boardSize = board_size**2))

        if not move_position.isnumeric():
            print("Please insert a number")
            continue

        if int(move_position) not in dict_board.keys():
            print("Position out of range. Please try again.")
            continue

        if not str(dict_board[int(move_position)]).isnumeric():
            print("Position already taken. Please try again")
            continue

        dict_board[int(move_position)] = player_symbol
        return dict_board


def check_win_condition(dict_board, board_size, dict_size):
    values = list(dict_board.values())
    horizontal_list = [values[i:i+board_size] for i in range(0, dict_size, board_size)]
    vertical_list = [values[i::board_size] for i in range(board_size)]
    leftright_digagonal = [values[i*(board_size+1)] for i in range(board_size)]
    rightleft_diagonal = [values[(i+1)*(board_size-1)] for i in range(board_size)]

    for chunk in horizontal_list:
        if len(set(chunk)) == 1:
            create_board(player_dict_board, player_board_size)
            print(f"Player {chunk[0]} Won!")
            return True

    for chunk in vertical_list:
        if len(set(chunk)) == 1:
            create_board(player_dict_board, player_board_size)
            print(f"Player {chunk[0]} Won!")
            return True

    if len(set(leftright_digagonal)) == 1:
        create_board(player_dict_board, player_board_size)
        print(f"Player {leftright_digagonal[0]} Won!")
        return True

    if len(set(rightleft_diagonal)) == 1:
        create_board(player_dict_board, player_board_size)
        print(f"Player {rightleft_diagonal[0]} Won!")
        return True

    if not any(item in list(range(1, dict_size)) for item in set(values)):
        create_board(player_dict_board, player_board_size)
        print("All sloth have been taken so no one won!")
        return True

    return False


player_board_size = define_boardsize()
player_dict_board = define_dict(player_board_size)
PLAYER_DICT_SIZE = len(player_dict_board) + 1

userOneSymbol, userTwoSymbol = define_usersymbol()
currentUser = userOneSymbol

while True:
    player_dict_board = user_decision(player_dict_board, currentUser, player_board_size)

    if check_win_condition(player_dict_board, player_board_size, PLAYER_DICT_SIZE):
        break

    if currentUser == userOneSymbol:
        currentUser = userTwoSymbol
    else:
        currentUser = userOneSymbol
