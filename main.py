from lib import board, game_init, state, move, pieces

def main():
    # ----- Game loop for testing -----
    state = game_init.new()
    while True:
        print(state.current_player, 'to move')
        state.board.print_board(state.current_player)
        x = input('Enter a square to select a piece to move. Give input in the format "a1", "e2", etc \n')
        state.move.move_from = state.board.algebra_dict[x]
        if state.move.is_piece():
            print('Select a square with a piece')
            continue
        piece = pieces.Piece(state)
        if piece.player != state.current_player:
            print('Select a piece of your own ya bellend')
            continue
        print(piece)
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
                state.board.list = state.make_move()
                if piece.name == 'KING':
                    False
                state.advance()
            else:
                print('Not a legal move, try again...')








if __name__ == "__main__":
    main()
