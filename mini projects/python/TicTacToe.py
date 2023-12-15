from termcolor import colored
board = [i for i in range(1, 10)]
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


def print_board():
    counter = 1
    for i in board:
        end = " "
        if counter % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(colored(f"[{i}]","yellow"), end=end)
        counter += 1


def make_move(brd, plyr, mv, undo=False):
    if can_move(brd, mv):
        brd[mv - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mv - 1] = mv
        return True, win
    return False, False


def has_empty_space():
    return board.count("X") + board.count("O") != 9


def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def can_move(brd, mv):
    if mv in range(1, 10) and isinstance(brd[mv - 1], int):
        return True
    return False


def computer_move():
    mv = -1
    # computer win chance check
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # player win chance check
    if mv == -1:
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                mv = i
    # move
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)

player, computer = "X", "O"
print("player: X\ncomputer: O")
while has_empty_space():
    print_board()
    move = int(input("choose your move(1--9) :"))
    moved, won = make_move(board, player, move)
    if not moved:
        print(colored("Invalid move try again", "red"))
        continue
    if won:
        print_board()
        print(colored("you win", "green"))
        break
    elif computer_move()[1]:
        print_board()
        print(colored("you lose", "red"))
        break
if not is_winner(board, player) and not is_winner(board, computer):
    print_board()
    print(colored("Draw!", "yellow"))
