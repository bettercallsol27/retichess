class Move:
    def __init__(self,gamestate):
        # Initialise a move
        # number wil be incremented with each move made. Somehow
        self.number = 0
        self.move_from = 0
        self.move_to = 0
        self.player = gamestate.current_player
        self.lst = gamestate.board.lst

    
    def is_on_board(self):
        # Function to return whether a square is on the board
        if self.lst[self.move_to] == 99:
            return False
        return True

    def is_empty(self): 
        if self.lst[self.move_to] == 0:
            return True

    def is_piece(self):
        if self.lst[self.move_from] == 0:
            return True
        else:
            return False

    def is_legal(self):
        # Legal move = Is player piece, Destination not outside play area, no friendly piece on destination, would not result in being in check. 
        destination_contents = self.lst[self.move_to]
        if self.is_on_board():
            if self.is_empty():
                return True
            else:
                if self.player == 'WHITE':
                    if destination_contents < 0:
                        # TODO add condition for being in check here
                        return True
                elif self.player == 'BLACK':
                    if destination_contents > 0:
                        return True
        return False

    # def is_promotion(self, Board):
    #     #Take the board array, self; returns True if promotion can occur otherwise False
    #     move_from = self.move_from
    #     move_to = self.move_to
    #     moving_piece = Board.list[move_from]
    #     if abs(moving_piece) == 1: # checks if piece moving is a pawn
    #         if moving_piece > 0: # checks if white or black pawn
    #             if str(move_to)[0] == 9: # checks if white pawn moving into promotion rank
    #                 return True
    #         else:
    #             if str(move_to)[0] == 2: # checks if black pawn moving into promotion rank
    #                 return True
    #     return False
