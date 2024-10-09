import os
import time
class Game:
    def __init__(self):
        self.__board = Board()
        self.__player1 = Player("Player 1", "X")
        self.__player2 = Player("Player 2", "O")
        self.__current_player = self.__player1
        self.__game_over = False

    def switch_turns(self):
        self.__current_player = self.__player2 if self.__current_player == self.__player1 else self.__player1

    def check_winner(self):
        if self.__board.check_winner(self.__current_player.get_symbol()):
            winner = (f"{self.__current_player.get_name()} wins............................................................................")
            for i in len(winner):
                time.sleep(0.5)
                print(winner[i])
            self.__game_over = True

    def play(self):
        while not self.__game_over:
            self.__board.display()
            try:
                row = int(input(f"{self.__current_player.get_name()}, enter row (0-2): "))
                col = int(input(f"{self.__current_player.get_name()}, enter column (0-2): "))

                if self.__board.make_move(row, col, self.__current_player):
                    self.check_winner()
                    if not self.__game_over:
                        self.switch_turns()
                else:
                    print("Invalid move - try again.")
            except ValueError:
                print("wrong!!!!!!!!!! 0-2 only!!")

        self.__board.display()
class Player:
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

class Board:
    def __init__(self, size=3):
        self.__size = size
        self.__grid = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        os.system('cls')
        for row in self.__grid:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.__grid[row][col] = player.get_symbol()
            return True
        return False

    def is_valid_move(self, row, col):
        return 0 <= row < self.__size and 0 <= col < self.__size and self.__grid[row][col] == ' '

    def is_full(self):
        for row in self.__grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    def check_winner(self, symbol):
        for row in self.__grid:
            if row.count(symbol) == self.__size:
                return True
        for col in range(self.__size):
            column = [self.__grid[row][col] for row in range(self.__size)]
            if column.count(symbol) == self.__size:
                return True

        diagonal1 = [self.__grid[i][i] for i in range(self.__size)]
        if diagonal1.count(symbol) == self.__size:
            return True

        diagonal2 = [self.__grid[i][self.__size - i - 1] for i in range(self.__size)]
        if diagonal2.count(symbol) == self.__size:
            return True

        return False

if __name__ == "__main__":
    game = Game()
    game.play()



