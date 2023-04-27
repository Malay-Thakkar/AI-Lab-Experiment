from math import inf as infinity
from random import choice
import platform
import time
from os import system
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

player = -1
computer = +1
steps = 1
turn = ""
status = "RUNNING..."


class stateNode:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    def evaluate(self):
        if self.wins(computer):
            score = +1
        elif self.wins(player):
            score = -1
        else:
            score = 0
        return score

    def game_over(self):
        return self.wins(player) or self.wins(computer)

    def empty_cells(self):
        cells = []
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells

    def valid_move(self, x, y):
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def wins(self, player):
        state = self.board
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def render(self, computer_choice, player_choice):
        global steps, turn, status
        chars = {-1: player_choice, +1: computer_choice, 0: ""}
        str_line = "---------------"

        print("\n" + str_line)

        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                print(f"| {symbol} |", end="")
            print("\n" + str_line)

        arr = np.zeros((3, 3), dtype=int)
        arr[1::2, 0::2] = 1
        arr[0::2, 1::2] = 1
        image = arr.reshape((3, 3))

        colors = ["blue", "yellow", "red", "green", "k", "#550011", "black", "orange"]

        cmap = ListedColormap(colors)
        plt.matshow(image, cmap=cmap)
        i, j = 0, 0

        for row in self.board:
            j = 0
            for cell in row:
                symbol = chars[cell]
                plt.text(
                    j,
                    i,
                    symbol,
                    va="center",
                    ha="center",
                    color="blue" if (i - j) % 2 == 0 else "green",
                    fontsize=30,
                )
                j += 1
            i += 1

        plt.xlabel(
            "step no.:-[{}] Turn:-[{}]\nchoice:- player[{}] computer[{}]".format(
                steps, turn, player_choice, computer_choice
            )
        )
        plt.ylabel("Status:- {}".format(status))
        plt.show()
        steps += 1


def minimax(state, depth, player):
    if player == computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or state.game_over():
        score = state.evaluate()
        return [-1, -1, score]

    for cell in state.empty_cells():
        x, y = cell[0], cell[1]
        state.board[x][y] = player
        score = minimax(state, depth - 1, -player)
        state.board[x][y] = 0
        score[0], score[1] = x, y

        if player == computer:
            if score[2] > best[2]:
                best = score  # max value

        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")


def computer_turn(state, computer_choice, player_choice):
    global turn
    turn = "COMPUTER"
    depth = len(state.empty_cells())
    if depth == 0 or state.game_over():
        return
    # clean()
    print(f"Computer turn[{computer_choice}]")
    state.render(computer_choice, player_choice)
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(state, depth, computer)
        x, y = move[0], move[1]
    state.set_move(x, y, computer)
    time.sleep(1)


def player_turn(state, computer_choice, player_choice):
    global turn
    turn = "player"
    depth = len(state.empty_cells())

    if depth == 0 or state.game_over():
        return

    move = -1
    moves = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
    }

    print(f"player turn [{player_choice}]")

    state.render(computer_choice, player_choice)
    while move < 1 or move > 9:
        try:
            move = int(input("Enter Any Number (1..9): "))
            coord = moves[move]
            can_move = state.set_move(coord[0], coord[1], player)
            if not can_move:
                print("Bad move")
                move = -1
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()

        except (KeyError, ValueError):
            print("Bad choice")


def main():

    player_choice = ""
    computer_choice = ""
    first = ""
    state = stateNode()

    while player_choice != "O" and player_choice != "X":
        try:
            player_choice = input("::Choose 'X' or 'O'::\nYour Choice: ").upper()
            print("")
        except (EOFError, KeyboardInterrupt):
            print("Program End")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")

        if player_choice == "X":
            computer_choice = "O"
        else:
            computer_choice = "X"

    while first != "Y" and first != "N":
        try:
            first = input("Do you want to start first? [Y/N]: ").upper()
        except (EOFError, KeyboardInterrupt):
            print("Program End")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")

    while len(state.empty_cells()) > 0 and not state.game_over():
        if first == "N":
            computer_turn(state, computer_choice, player_choice)
            first = ""
        player_turn(state, computer_choice, player_choice)
        computer_turn(state, computer_choice, player_choice)

    global status
    if state.wins(player):
        print(f"player turn [{player_choice}]")
        status = "player WINS!"
        state.render(computer_choice, player_choice)
        print(status)
    elif state.wins(computer):
        print(f"Computer turn [{computer_choice}]")
        status = "COMPUTER WINS"
        state.render(computer_choice, player_choice)
        print(status)
    else:
        status = "DRAW!"
        state.render(computer_choice, player_choice)
        print(status)
    exit()


if __name__ == "__main__":
    main()
