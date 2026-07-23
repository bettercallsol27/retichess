import boardstate

class Pawn:
    def __init__(self, location, player):
        self.moveset = [10,20,9,11]
        self.location = location
        self.player = player

    def find_moves(self):
        False

class Knight:
    def __init__(self, location, player):
        self.moveset = [8,12,19,21,-8,-12,-19,-21]
        self.location = location
        self.player = player

class Bishop:
    def __init__(self, location, player):
        self.moveset = [9,11,-9,11]
        self.location = location
        self.player = player

    def find_moves(self):
            False

class Castle:
    def __init__(self, location, player):
        self.moveset = [10,1,-10,-1]
        self.location = location
        self.player = player

    def find_moves(self):
            False

class Queen:
    def __init__(self, location, player):
        self.moveset = [9,11,-9,11,10,1,-10,-1]
        self.location = location
        self.player = player

    def find_moves(self):
            False

class King:
    # create new instances of King, accepting player being either Player.WHITE or Player.BLACK
    # used to track location and possibly "in check" status, tbd
    def __init__(self, player):
        self.moveset = [1,9,10,11,-1,-9,-10,-11]
        if player is boardstate.Player.WHITE:
            self.player = boardstate.Player.WHITE
            self.location = 25
            self.in_check = False
        elif player is boardstate.Player.BLACK:
            self.player = boardstate.Player.BLACK
            self.location = 95
            self.in_check = False
        else:
            # Unsure how to do error handling in Python right now lmao
            False
    
    def update_location(self, Move):
        # Change location to new square when moved, new location provided by Move
        self.location = Move.move_to

    #def is_check(self, Board):
        # WIP function kms, checks if player is in check for board state self, returning true or false
        # False
        # I have no earthly fucking clue how to go about testing for being in check, that sounds like a lot of work.
        # I'll get round to it. Probably checking if move_from is on the ray path of an opposing piece or some such
        # Cast rays on a loop from king? For diagonal rays check each square for opposing Queen or Bishop, for linear rays check for Castle or Queen.
        # If any other piece encountered they would be blocking the ray, so quit that ray loop
