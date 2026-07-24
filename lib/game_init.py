from lib import state, board, move


def new():
    start_state = state.GameState()
    game_board = board.GameBoard()
    danger_board = board.DangerBoard()
    first_move = move.Move(game_board.list)
    start_state.move = first_move
    start_state.current_player = 'WHITE'
    start_state.board = game_board
    start_state.danger_board = danger_board
    start_state.king_moves = state.KingMoves(game_board.list)
    start_state.knight_moves = state.KnightMoves(game_board.list)
    return start_state
