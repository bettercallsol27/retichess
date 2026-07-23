from boardstate import Board, Enum, GameState, Move, Player, KnightMoves
from movement import ChessPieces, PieceMoves, Piece

def main():
    state = GameState()
    while True:
        print(state.current_player.value, 'to move')
        state.board.print_board(state.current_player)
        x = input('Enter a square to select a piece to move. Give input in the format "a1", "e2", etc \n')
        state.move.move_from = state.board.algebra_dict[x]
        piece = Piece(state.move.move_from,state)
        if piece.player != state.current_player:
            print('Select a piece of your own ya bellend')
            continue
        piece.find_moves()
        if piece.moves_list == []:
            print('No legal moves, select another piece')
            continue
        legal = False
        while legal == False:
            y = input('Enter a square to move to from list of allowed moves. Give input in the format "a1", "e2", etc \n')
            print(y, state.board.algebra_dict[y])
            if state.board.algebra_dict[y] in piece.moves_list:
                legal = True
                state.move.move_to = state.board.algebra_dict[y]
                state.board.list = state.board.make_move(state.move)
                state.advance()
            else:
                print('Not a legal move, try again...')








if __name__ == "__main__":
    main()
