import unittest
from Board.Board import BoardClass
from Validator.MoveValidator import MoveValidatorClass
from Player.Human import HumanClass


class TestValidator(unittest.TestCase):

    #This method gets called before starting every test
    #It creates the board
    def setUp(self: object) -> None:
        self.Board = BoardClass()
        self.MoveValidator = MoveValidatorClass()
        self.player1 = HumanClass(1)

    # Testing if a move is correct
    # Player's inputs are converted into strings automatically by input()


    def test_CheckIfColumnIsNotFull(self):

        #Fill the second column with 5 tokens
        for i in range(0,5):
            self.Board.AddToken(1, self.player1)

        is_column_not_full = self.MoveValidator.CheckIfColumnIsNotFull(1, self.Board)

        if is_column_not_full:
            self.assertEqual(is_column_not_full, True)
        

        #self.Board.UpdateBoard()


    def test_CheckIfColumnIsFull(self):

        #Fill the second column with 6 tokens (max)
        for i in range(0,6):
            self.Board.AddToken(1, self.player1)

        is_column_not_full = self.MoveValidator.CheckIfColumnIsNotFull(1, self.Board)

        if is_column_not_full:
            self.assertEqual(is_column_not_full, False)
        