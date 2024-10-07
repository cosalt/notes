class Game:
    def __init__(self):
        self.__player1 = player1
        self.__player2 = player2
        self.__currentturn = currentplayer
        self.__game_over = game_over

    def switch_turns(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_winner(self, player):
        if player not in ["0", "X"]:
            print("not valid!")

        """winning_grids = [
            [[0,0],[0,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[2,0],[2,1],[2,2]],
            
            [[0,0],[1,0][2,0]
        ]"""
    def play(self):
        while not self.game_over:
            print(f"Current player: {self.current_player.name}")
class Player:
    def __init(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[' ' for i in range(size)] for i in range(size)]

    def display(self):

