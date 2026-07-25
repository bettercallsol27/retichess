from lib.game import Game
import sys

def main():
    # ----- Game loop for testing -----
    while True:
        print('Start a new game or load a game? Enter "new" or "load" respectively')
        y = input('Alternatively, enter "quit" to quite the program \n').lower()
        if y == 'quit':
            sys.exit()
        else:
            if y == 'new':
                game = Game.new()
            elif y == 'load':
                False

        print(game.current_player, 'to move')
        game.board.print_board(game.current_player)
        x = input('Enter a square to select a piece to move. Give input in the format "a1", "e2", etc \n')
        game.move.move_from = game.board.algebra_dict[x]

        if game.move.is_piece():
            print('Select a square with a piece')
            continue
        piece = Game.new_piece(game)
        if piece.player != game.current_player:
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
