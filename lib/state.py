from enum import Enum
# from lib.pieces import *

class State:
    # Fresh game state, initialised at the start of every new or loaded game
    def __init__(self):
        self.current_player = 'WHITE'
        self.count = 0

    def name(self, name):
        self.name = input('Please enter a name for this game. \n')
    
    def switch_player(self):
        if self.current_player == Player.WHITE:
            self.current_player = Player.BLACK
        else:
            self.current_player = Player.WHITE
    
    def advance(self):
        self.count += 1
        self.switch_player()
    
    def make_move(self):
        # Take the board array and a Move, changing self.lsit to match the state after move made
        self.lst[self.move.move_to] = self.lst[self.move.move_from]
        list[move.move_from] = 0
        return list


class KnightMoves:
    # Initialise a dict of all possible knight moves
    # Do this on startup
    def __init__(self,list):
        board = list
        self.dict = {}
        for i in range(21,98):
            moveset = [8,19,21,12,-8,-19,-21,-12]
            move_list = []
            for x in moveset:
                if board[i + x] != 99:
                    move_list.append(i+x)
            self.dict[i] = move_list
        print(self.dict)

class KingMoves:
    # Initialise a dict of all possible King moves
    # Do this on startup
    def __init__(self,list):
        board = list
        self.dict = {}
        for i in range(21,98):
            moveset = [1,-1,9,-9,10,-10,11,-11]
            move_list = []
            for x in moveset:
                if board[i + x] != 99:
                    move_list.append(i+x)
            self.dict[i] = move_list
        print('king moves: ',self.dict)    

class Player(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"

# ON USING ENUMS - BASICS
# class Color(Enum):
#      RED = 1
#      BLUE = 2
#      GREEN = 3
#     attribute access:
#         Color.RED <Color.RED: 1>
#     value lookup:
#         Color(1) -> <Color.RED: 1>
#     name lookup:
#         Color['RED'] <Color.RED: 1>