from enum import Enum

class ChessPieces(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    CASTLE = 4
    QUEEN = 5
    KING = 6

# class PieceNames(Enum):
#     PAWN = ChessPieces.PAWN
#     KNIGHT = ChessPieces.KNIGHT
#     BISHOP = ChessPieces.BISHOP
#     CASTLE = ChessPieces.CASTLE
#     QUEEN = ChessPieces.QUEEN
#     KING = ChessPieces.KING

class PieceMoves(Enum):
    PAWN = [10,20,9,11]
    KNIGHT = [8,12,19,21,-8,-12,-19,-21]
    BISHOP = [9,11,-9,-11]
    CASTLE = [10,1,-10,-1]
    QUEEN = [9,11,-9,-11,10,1,-10,-1]
    KING = [1,9,10,11,-1,-9,-10,-11]

class Piece:
    def __init__(self,game):
        self.game = game
        self.home = game.move.move_from
        self.name = ChessPieces(abs(self.lst[self.home])).name
        self.value = ChessPieces(abs(self.lst[self.home])).value
        self.moveset = PieceMoves[self.name].value
        self.moves_list = []
        if self.lst[self.home] > 0:
            self.player = 'WHITE'
        else:
            self.player = 'BLACK'

    def find_moves(self):
        state = self.state
        move = state.move
        if self.name == 'PAWN':
            self.pawn()
        # elif self.name == 'KNIGHT':
        #     for i in state.knight_moves.dict[self.home]:
        #         move.move_to = i
        #         if move.is_legal():
        #             self.moves_list.append(i)
        # elif self.name == 'KING':
        #     for i in state.king_moves.dict[self.home]:
        #         move.move_to = i
        #         if move.is_legal():
        #             self.moves_list.append(i)
        # elif self.name == 'QUEEN':
        #     self.ray_moves()
        # elif self.name == 'BISHOP':
        #     self.ray_moves()
        # elif self.name == 'CASTLE':
        #     self.ray_moves()

#     def homerow(self):
#         state = self.state
#         move = state.move
#         go = True
#         if self.player == Player.WHITE:
#             while go == True:
#                 for i in (self.moveset[0],self.moveset[1]):
#                     x = self.home
#                     x += i
#                     move.move_to = x
#                     if move.is_legal():
#                         self.moves_list.append(x)
#                     else:
#                         go = False
#                 go = False 
#         else:
#             while go == True:
#                 for i in (self.moveset[0],self.moveset[1]):
#                     x = self.home
#                     x -= i
#                     move.move_to = x
#                     if move.is_legal():
#                         self.moves_list.append(x)
#                     else:
#                         go = False
#                 go = False 

#     def pawn(self):
#         state = self.state
#         move = state.move
#         home = self.home
#         # ----- Logic for White Pawns -----
#         if self.player == Player.WHITE:
#             # ----- Logic for pawn on homerow
#             if str(home)[0] == '3':
#                 self.homerow()
#             # ----- Logic for Pawn not on homerow
#             elif str(home)[0] != '3':
#                 x = self.home
#                 x += self.moveset[0]
#                 move.move_to = x
#                 if move.is_legal() and self.list[x] == 0:
#                     self.moves_list.append(x)
#             for i in (self.moveset[2],self.moveset[3]):
#                 x = self.home
#                 x += i
#                 move.move_to = x
#                 if move.is_legal() and self.list[x] != 0:
#                     self.moves_list.append(x)

                        
#         # ----- Logic for Black Pawns -----
#         elif self.player == Player.BLACK:
#             # ----- Logic for pawn on homerow
#             if str(home)[0] == '8':
#                 self.homerow()
#             # ----- Logic for Pawn not on homerow
#             else:
#                 x = self.home
#                 x -= self.moveset[0]
#                 move.move_to = x
#                 if move.is_legal() and self.list[x] == 0:
#                     self.moves_list.append(x)
#                 for i in (self.moveset[2],self.moveset[3]):
#                     x = self.home
#                     x -= i
#                     move.move_to = x
#                     if move.is_legal() and self.list[x] != 0:
#                         self.moves_list.append(x)

#     def ray_moves(self):
#         print('Find ray moves')
#         state = self.state
#         move = state.move
#         print(self.moveset)
#         for i in self.moveset:
#             x = self.home
#             go = True
#             while go == True:
#                 x += i
#                 move.move_to = x
#                 print(move.move_from, move.move_to)
#                 if move.is_legal():
#                     self.moves_list.append(x)
#                 else:
#                     print('Move not legal')
#                     go = False

# class King:
#     # create new instances of King, accepting player being either Player.WHITE or Player.BLACK
#     # used to track location and possibly "in check" status, tbd
#     def __init__(self,player):
#         self.moveset = [1,9,10,11,-1,-9,-10,-11]
#         if player is Player.WHITE:
#             self.player = Player.WHITE
#         elif player is Player.BLACK:
#             self.player = Player.BLACK
#         self.in_check = False

