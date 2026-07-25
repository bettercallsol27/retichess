from lib.state import State, KingMoves, KnightMoves, Player
from lib.board import GameBoard, DangerBoard
from lib.move import Move
from lib.pieces import Piece

class Game:
    def new():
        start_state = State()
        start_state.board = GameBoard()
        first_move = Move(start_state)
        start_state.move = first_move
        start_state.king_moves = KingMoves(start_state.board.lst)
        start_state.knight_moves = KnightMoves(start_state.board.lst)
        start_state.name = input('Please enter a name for this game. \n')
        return start_state

    def load():
        False
    
    def new_piece(gamestate):
        obj = Piece(gamestate)
        return obj

class InputHandler:
    False


