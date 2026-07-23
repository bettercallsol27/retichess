from enum import Enum
from pieces import *

class Board:
    def __init__(self):
        
        # Initialise a new board from start of play
        # "99" represents squares which are off the board
        # Values can be understood as {0 : Empty Square, 1 : Pawn, 2 : Knight, 3 : Bisop, 4 : Castle, 5 : Queen, 6 : King}
        # +ive pieces values are the White side, -ive piece values are the Black side
        # self.list[21] ~= a1, self.list[22] ~= b1, etc. This convention will be followed throughout the program
        self.list = [
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 4, 2, 3, 5, 6, 3, 2, 4, 99,
                    99, 1, 1, 1, 1, 1, 1, 1, 1, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, -1, -1, -1, -1, -1, -1, -1, -1, 99,
                    99, -4, -2, -3, -5, -6, -3, -2, -4, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99]

        self.algebra_dict = {
                    'a1':21, 'b1':22, 'c1':23 ,'d1':24 , 'e1':25 , 'f1':26, 'g1':27 , 'h1':28 ,
                    'a2':31, 'b2':32, 'c2':33 ,'d2':34 , 'e2':35 , 'f2':36, 'g2':37 , 'h2':38 ,
                    'a3':41, 'b3':42, 'c3':43 ,'d3':44 , 'e3':45 , 'f3':46, 'g3':47 , 'h3':48 ,
                    'a4':51, 'b4':52, 'c4':53 ,'d4':54 , 'e4':55 , 'f4':56, 'g4':57 , 'h4':58 ,
                    'a5':61, 'b5':62, 'c5':63 ,'d5':64 , 'e5':65 , 'f5':66, 'g5':67 , 'h5':68 ,
                    'a6':71, 'b6':72, 'c6':73 ,'d6':74 , 'e6':75 , 'f6':76, 'g6':77 , 'h6':78 ,
                    'a7':81, 'b7':82, 'c7':83 ,'d7':84 , 'e7':85 , 'f7':86, 'g7':87 , 'h7':88 ,
                    'a8':91, 'b8':92, 'c8':93 ,'d8':94 , 'e8':95 , 'f8':96, 'g8':97 , 'h8':98 ,
                }

        self.square_dict = {
                    21:'a1', 22:'b1', 23:'c1' ,24:'d1' , 25:'e1' , 26:'f1', 27:'g1' , 28:'h1' ,
                    31:'a2', 32:'b2', 33:'c2' ,34:'d2' , 35:'e2' , 36:'f2', 37:'g2' , 38:'h2' ,
                    41:'a3', 42:'b3', 43:'c3' ,44:'d3' , 45:'e3' , 46:'f3', 47:'g3' , 48:'h3' ,
                    51:'a4', 52:'b4', 53:'c4' ,54:'d4' , 55:'e4' , 56:'f4', 57:'g4' , 58:'h4' ,
                    61:'a5', 62:'b5', 63:'c5' ,64:'d5' , 65:'e5' , 66:'f5', 67:'g5' , 68:'h5' ,
                    71:'a6', 72:'b6', 73:'c6' ,74:'d6' , 75:'e6' , 76:'f6', 77:'g6' , 78:'h6' ,
                    81:'a7', 82:'b7', 83:'c7' ,84:'d7' , 85:'e7' , 86:'f7', 87:'g7' , 88:'h7' ,
                    91:'a8', 92:'b8', 93:'c8' ,94:'d8' , 95:'e8' , 96:'f8', 97:'g8' , 98:'h8' ,
                }

    def make_move(self, Move):
        # Take the board array and a Move [move number, move_from, move_to, player], changing self.lsit to match the state after move made
        # print('move from', Move.move_from, 'move to', Move.move_to)
        self.list[Move.move_to] = self.list[Move.move_from]
        self.list[Move.move_from] = 0
        return self.list
    
    def print_board(self, player): # Print out the board from either player's perspective
        arg = [0,0,0,0,0,0,0,0]
        if player == Player.WHITE:
            z = 98
            p = 98
            for y in range(0,8):
                for x in (7,6,5,4,3,2,1,0):
                    arg[x] = self.list[z]
                    z -= 1
                print(arg)
                z = p - 10
                p = z
                arg = [0,0,0,0,0,0,0,0]
        elif player == Player.BLACK:
            z = 21
            p = 21
            for y in range(0,8):
                for x in (7,6,5,4,3,2,1,0):
                    arg[x] = self.list[z]
                    z += 1
                print(arg)
                z = p + 10
                p = z
                arg = [0,0,0,0,0,0,0,0]


class Move:
    def __init__(self,player,number):
        # Initialise a move
        # number wil be incremented with each move made. Somehow
        self.number = number
        self.move_from = 0
        self.move_to = 0
        self.player = player
    
    def is_on_board(self, list):
        # Function to return whether a square is on the board
        if list[self.move_to] == 99:
            return False
        return True

    def is_legal(self, list):
        # Take self, list
        # Legal move = Is player piece, Destination not outside play area, no friendly piece on destination, would not result in being in check. 
        destination_contents = list[self.move_to]
        if self.is_on_board(list):
            if destination_contents == 0:
                return True
            if self.player is Player.WHITE:
                if destination_contents < 0:
                    # TODO add condition for being in check here
                    return True
            else:
                if destination_contents > 0:
                    return True
        return False

    def is_promotion(self, Board):
        #Take the board array, self; returns True if promotion can occur otherwise False
        move_from = self.move_from
        move_to = self.move_to
        moving_piece = Board.list[move_from]
        if abs(moving_piece) == 1: # checks if piece moving is a pawn
            if moving_piece > 0: # checks if white or black pawn
                if str(move_to)[0] == 9: # checks if white pawn moving into promotion rank
                    return True
            else:
                if str(move_to)[0] == 2: # checks if black pawn moving into promotion rank
                    return True
        return False


class GameState: # TBD if this stays
    def __init__(self):
        self.current_player = Player.WHITE
        self.white_king = King(Player.WHITE)
        self.black_king = King(Player.BLACK)
        self.board = Board()
        self.count = 0
        self.knight_moves = KnightMoves()
        self.king_moves = KingMoves()
        self.move = Move(self.count,self.current_player)

    def name(self, name):
        self.name = name
    
    def toggle_player(self):
        if self.current_player == Player.WHITE:
            self.current_player = Player.BLACK
        else:
            self.current_player = Player.WHITE

    def advance(self):
        self.count += 1
        self.toggle_player()

class KnightMoves:
    # Initialise a dict of all possible knight moves
    # Do this on startup
    def __init__(self):
        board = Board()
        self.dict = {}
        for i in range(21,98):
            knight = Knight(i, Player.WHITE)
            move_list = []
            for x in knight.moveset:
                if board.list[i + x] != 99:
                    move_list.append(i+x)
            self.dict[i] = move_list
        print(self.dict)

class KingMoves:
    # Initialise a dict of all possible King moves
    # Do this on startup
    def __init__(self):
        board = Board()
        self.dict = {}
        for i in range(21,98):
            king = King(Player.WHITE)
            move_list = []
            for x in king.moveset:
                if board.list[i + x] != 99:
                    move_list.append(i+x)
            self.dict[i] = move_list
        print('king moves: ',self.dict)    

class Player(Enum):
    WHITE = "White"
    BLACK = "Black"