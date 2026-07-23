from boardstate import Board as Board, GameState as GameState, King as King, Move as Move, Player as Player
from enum import Enum
import unittest

class Methods(unittest.TestCase):

    def test_move(self):
        move1 = Move(1,0,0,Player.WHITE)
        pre_move1 = Board('pre_move1')
        post_move1 = Board('post_move1')
        self.assertEqual(pre_move1.list, post_move1.list) # 0 move made, boards are the same

        move = Move(1,35,55,Player.WHITE)
        board1 = Board('pre_move')
        board2 = board1.make_move(move)
        self.assertNotEqual(board1.list[55], board2.list[55]) # e2 -> e4, e2 no longer equal between board states
        self.assertEqual(board1.list[35], board2.list[55]) # e2 -> e4, e2 pre-move now equals e4 post-move

    def test_islegal(self):
        move1 = Move(1,90,91,Player.WHITE) # Should be True
        move2 = Move(1,90,100,Player.WHITE) # Should be False
        board = Board('legal')
        self.assertTrue(board.is_on_board(move1))
        self.assertFalse(board.is_on_board(move2))

if __name__ == '__main__':
    unittest.main()
