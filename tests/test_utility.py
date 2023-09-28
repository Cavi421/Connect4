import unittest
from Board.Board import BoardClass
from Validator.MoveValidator import MoveValidatorClass
from Player.Human import HumanClass
from Utility.Utility import UtilityClass


class TestValidator(unittest.TestCase):
    # This method gets called before starting every test
    # It creates the board
    def setUp(self: object) -> None:
        self.Board = BoardClass()
        self.player1 = HumanClass(1)
        self.Utility = UtilityClass()

    def test_ScanMatrixColumnForEmptyPositionId(self: object) -> None:
        for i in range(0, 3):
            self.Board.AddToken(0, self.player1)

        # First empty spot in this case is the 4th row from below, which converted is the row_index 2
        first_empty_spot_row_id = self.Utility.ScanMatrixColumnForEmptyPositionId(
            0, self.Board
        )

        # self.Board.UpdateBoard()

        self.assertEqual(first_empty_spot_row_id, 2)

    def test_ScanMatrixColumnForEmptyPositionId_WhenColumnIsFull(self: object) -> None:
        # Fill a column
        for i in range(0, 7):
            self.Board.AddToken(0, self.player1)

        # First empty spot in this case doesn't exist because column is full.
        # So the method returns -1. Other checks are performed usually before this one
        # So the -1 won't get used in the game
        # Remove with refactoring
        first_empty_spot_row_id = self.Utility.ScanMatrixColumnForEmptyPositionId(
            0, self.Board
        )

        # self.Board.UpdateBoard()

        self.assertEqual(first_empty_spot_row_id, -1)

    def test_ScanMatrixColumnToSeeIfIsNotFull(self: object) -> None:
        # Fill a column with 3 tokens
        for i in range(0, 3):
            self.Board.AddToken(0, self.player1)

        # Check if there is at least one empty spot
        is_column_not_full = self.Utility.ScanMatrixColumnToSeeIfIsNotFull(
            0, self.Board
        )

        self.assertEqual(is_column_not_full, True)

    def test_ScanMatrixColumnToSeeIfIsNotFull_WhenColumnIsFull(self: object) -> None:
        # Fill a column with 3 tokens
        for i in range(0, 7):
            self.Board.AddToken(0, self.player1)

        # Check if there is at least one empty spot
        is_column_not_full = self.Utility.ScanMatrixColumnToSeeIfIsNotFull(
            0, self.Board
        )

        self.assertEqual(is_column_not_full, False)
