import unittest
from Board.Board import BoardClass
from Validator.MoveValidator import MoveValidatorClass
from Player.Human import HumanClass


class TestValidator(unittest.TestCase):
    # This method gets called before starting every test
    # It creates the board
    def setUp(self: object) -> None:
        self.Board = BoardClass()
        self.player1 = HumanClass(1)

    def test_AddToken(self: object) -> None:
        # Add token in column at column 0.
        # Since there are no other tokens, it'll get added at [0][5] (at the bottom)
        last_move_cell_row, last_move_cell_column = self.Board.AddToken(0, self.player1)

        # Expect that player's id 1 is now in [0][5]
        last_move_current_value = self.Board.matrix_board[last_move_cell_row][last_move_cell_column]

        # Value is 1 because passed 1 to HumanClass()
        self.assertEqual(last_move_current_value, 1)


    def test_ComputeTokenPosition_OnNotFullColumn(self: object) -> None:

        #Add token in first column at row 5, because it's first empty spot
        self.Board.AddToken(0, self.player1)

        #Check if token would be added in row 4 on first column
        #so empty_position_row_id should be equal to 4
        empty_position_row_id = self.Board.ComputeTokenPosition(0)

        self.assertEqual(empty_position_row_id, 4)


    def test_ComputeTokenPosition_OnFullColumn(self: object) -> None:

        #Fill the first column with 6 tokens -> full comlumn
        for i in range(0,6):
            self.Board.AddToken(0, self.player1)

        #self.Board.UpdateBoard()

        #Check if token would be added in row 0 which is currently full
        #Returns -1 which means that the token won't be added.
        #In reality there are other checks that makes sure that a token
        #won't be added on a full column. So this -1 is never utilized.
        #Refactoring the code will probably remove this test
        empty_position_row_id = self.Board.ComputeTokenPosition(0)

        self.assertEqual(empty_position_row_id, -1)
