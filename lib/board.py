from enum import Enum

class Player(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"


class GameBoard:
    def __init__(self):
        
        # Initialise a new board from start of play
        # "99" represents squares which are off the board
        # Values can be understood as {0 : Empty Square, 1 : Pawn, 2 : Knight, 3 : Bisop, 4 : Castle, 5 : Queen, 6 : King}
        # +ive pieces values are the White side, -ive piece values are the Black side
        # self.list[21] ~= a1, self.list[22] ~= b1, etc. This convention will be followed throughout the program
        # self.list = [
        #             99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
        #             99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
        #             99, 4, 2, 3, 5, 6, 3, 2, 4, 99,
        #             99, 1, 1, 1, 1, 1, 1, 1, 1, 99,
        #             99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
        #             99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
        #             99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
        #             99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
        #             99, -1, -1, -1, -1, -1, -1, -1, -1, 99,
        #             99, -4, -2, -3, -5, -6, -3, -2, -4, 99,
        #             99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
        #             99, 99, 99, 99, 99, 99, 99, 99, 99, 99]

        self.lst = [
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 0, 2, 3, 4, 5, 6, 0, 0, 99,
                    99, 1, 2, 0, 3, 0, 0, 0, 0, 99,
                    99, 1, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99]

        # a1:21
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
        # 21:a1
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
    
    def print_board(self, player): # Print out the board from either player's perspective
        arg = [0,0,0,0,0,0,0,0]
        if player == 'WHITE':
            z = 98
            p = 98
            for y in range(0,8):
                for x in (7,6,5,4,3,2,1,0):
                    arg[x] = self.lst[z]
                    z -= 1
                print(arg)
                z = p - 10
                p = z
                arg = [0,0,0,0,0,0,0,0]
        elif player == 'BLACK':
            z = 21
            p = 21
            for y in range(0,8):
                for x in (7,6,5,4,3,2,1,0):
                    arg[x] = self.lst[z]
                    z += 1
                print(arg)
                z = p + 10
                p = z
                arg = [0,0,0,0,0,0,0,0]


class DangerBoard:
    def __init__(self):
        self.list = [
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 0, 0, 0, 0, 0, 0, 0, 0, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
                    99, 99, 99, 99, 99, 99, 99, 99, 99, 99]


    # def find_danger(self):
    #     state = self.state
    #     board = state.board.list
    #     current_player = state.current_player
    #     move = self.move
    #     if current_player == Player.WHITE:
    #         for i in range(21,98):
    #             if board[i] == 0 | board[i] > 0:
    #                 continue
    #             elif board[i] < 0: # ----- Important section
    #                 move.move_from = i
    #                 val = abs(board[i])
    #                 piece = ChessPieces(val).name
    #                 if piece == 'PAWN':

    #                     list = self.danger_pieces(piece)
    #                 False
        
    #     elif current_player == Player.BLACK:
    #         for i in range(21,98):
    #             if board[i] == 0 | board[i] < 0:
    #                 continue
    #             elif board[i] > 0: # ----- Important section
    #                 move.move_from = i
    #                 False
        
    # def danger_pieces(self,piece):
    #     state = self.state
    #     board = state.list
    #     move = self.move
    #     if piece == 'PAWN':
    #         for i in (9,11):
    #             False
    #     elif piece == 'KNIGHT':
    #         for i in state.knight_moves.dict[self.home]:
    #             move.move_to = i
    #             if move.is_legal() and board[i] == 0:
    #                 self.moves_list.append(i)
    #     elif piece == 'KING':
    #         for i in state.king_moves.dict[self.home]:
    #             move.move_to = i
    #             if move.is_legal() and self.list[i] == 0:
    #                 self.moves_list.append(i)
    #     elif piece == 'QUEEN':
    #         self.ray_moves()
    #     elif piece == 'BISHOP':
    #         self.ray_moves()
    #     elif piece == 'CASTLE':
    #         self.ray_moves()

    # def danger_rays(self):
        # print('Find danger spaces from ray move pieces')
        # move = self.move
        # state = self.state
        # print(self.moveset)
        # for i in self.moveset:
        #     x = self.home
        #     go = True
        #     while go == True:
        #         x += i
        #         move.move_to = x
        #         print(move.move_from, move.move_to)
        #         if move.is_legal():
        #             self.list[x] = 1
        #         else:
        #             print('Move not legal')
        #             go = False