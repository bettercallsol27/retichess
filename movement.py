from boardstate import Board, Enum, GameState, Move, Player
from enum import Enum

class ChessPieces(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    CASTLE = 4
    QUEEN = 5
    KING = 6

class PieceNames(Enum):
    PAWN = ChessPieces.PAWN
    KNIGHT = ChessPieces.KNIGHT
    BISHOP = ChessPieces.BISHOP
    CASTLE = ChessPieces.CASTLE
    QUEEN = ChessPieces.QUEEN
    KING = ChessPieces.KING

class PieceMoves(Enum):
    PAWN = [10,20,9,11]
    KNIGHT = [8,12,19,21,-8,-12,-19,-21]
    BISHOP = [9,11,-9,11]
    CASTLE = [10,1,-10,-1]
    QUEEN = [9,11,-9,11,10,1,-10,-1]
    KING = [1,9,10,11,-1,-9,-10,-11]

class Piece:
    def __init__(self, location, state):
        self.state = state
        self.list = state.board.list
        self.location = location
        self.name = ChessPieces(abs(self.list[location])).name
        self.value = ChessPieces(abs(self.list[location])).value
        self.moveset = PieceMoves[self.name].value
        self.moves_list = []
        if self.list[location] > 0:
            self.player = Player.WHITE
        else:
            self.player = Player.BLACK
        self.move = Move(self.player,self.state.count)
        self.move.move_from = self.location

    def find_moves(self):
        if self.name == 'PAWN':
            self.pawn()
        elif self.name == 'KNIGHT':
            for i in self.state.knight_moves.dict[self.location]:
                self.move.move_to = i
                if self.move.is_legal(self.list) and self.list[i] == 0:
                    self.moves_list.append(i)
        elif self.name == 'KING':
            for i in self.state.king_moves.dict[self.location]:
                self.move.move_to = i
                if self.move.is_legal(self.list) and self.list[i] == 0:
                    self.moves_list.append(i)
        elif self.name == 'QUEEN':
            False
        elif self.name == 'BISHOP':
            False
        elif self.name == 'CASTLE':
            False
        print(self.moves_list)

    def homerow(self):
        home = self.location
        go = True
        if self.player == Player.WHITE:
            while go == True:
                for i in (self.moveset[0],self.moveset[1]):
                    x = self.location
                    x += i
                    self.move.move_to = x
                    if self.move.is_legal(self.list) and self.list[x] == 0:
                        self.moves_list.append(x)
                    else:
                        go = False
                go = False 
        else:
            while go == True:
                for i in (self.moveset[0],self.moveset[1]):
                    x = self.location
                    x -= i
                    self.move.move_to = x
                    if self.move.is_legal(self.list) and self.list[x] == 0:
                        self.moves_list.append(x)
                    else:
                        go = False
                go = False 

    def pawn(self):
        home = self.location
        # ----- Logic for White Pawns -----
        if self.player == Player.WHITE:
            # ----- Logic for pawn on homerow
            if str(home)[0] == '3':
                self.homerow()
            # ----- Logic for Pawn not on homerow
            else:
                x = self.location
                x += self.moveset[0]
                self.move.move_to = x
                if self.move.is_legal(self.list) and self.list[x] == 0:
                    self.moves_list.append(x)
            for i in (self.moveset[2],self.moveset[3]):
                x = self.location
                x += i
                self.move.move_to = x
                if self.move.is_legal(self.list) and self.list[x] != 0:
                    self.moves_list.append(x)

                        
        # ----- Logic for Black Pawns -----
        elif self.player == Player.BLACK:
            # ----- Logic for pawn on homerow
            if str(home)[0] == '8':
                self.homerow()
            # ----- Logic for Pawn not on homerow
            else:
                x = self.location
                x -= self.moveset[0]
                self.move.move_to = x
                if self.move.is_legal(self.list) and self.list[x] == 0:
                    self.moves_list.append(x)
                for i in (self.moveset[2],self.moveset[3]):
                    x = self.location
                    x -= i
                    self.move.move_to = x
                    if self.move.is_legal(self.list) and self.list[x] != 0:
                        self.moves_list.append(x)

    def ray_moves(self):
        print(self.moveset)
        home = self.location
        x = self.location
        for i in self.moveset:
            go = True
            while go == True:
                x += i
                print(x)
                if Move(1,home,x,self.color).is_legal(self.list):
                    self.moves_list.append(x)
                else:
                    print('Move not legal')
                    go = False




