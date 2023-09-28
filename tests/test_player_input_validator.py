import unittest
from Board.Board import BoardClass
from Validator.PlayerInputValidator import PlayerInputValidatorClass


class TestValidator(unittest.TestCase):

    #This method gets called before starting every test
    #It creates the board
    def setUp(self: object) -> None:
        self.Board = BoardClass()
        self.PlayerInputValidator = PlayerInputValidatorClass()

    # Testing if the Player's inputs fails the sanity checks
    # Player's inputs are converted into strings automatically by input()

    def test_IsNotEmpty(self):
        self.PlayerInputValidator.choosen_column = ""
        is_not_empty = self.PlayerInputValidator.IsNotEmpty()

        self.assertEqual(is_not_empty, False)


        self.PlayerInputValidator.choosen_column = "dydu"
        is_not_empty = self.PlayerInputValidator.IsNotEmpty()

        self.assertEqual(is_not_empty, True)


        self.PlayerInputValidator.choosen_column = "6"
        is_not_empty = self.PlayerInputValidator.IsNotEmpty()

        self.assertEqual(is_not_empty, True)


    def test_IsInt(self):
        self.PlayerInputValidator.choosen_column = "ddsfs"
        is_int = self.PlayerInputValidator.IsInt()

        self.assertEqual(is_int, False)

        self.PlayerInputValidator.choosen_column = "1.2"
        is_int = self.PlayerInputValidator.IsInt()

        self.assertEqual(is_int, False)

        self.PlayerInputValidator.choosen_column = "7"
        is_int = self.PlayerInputValidator.IsInt()

        self.assertEqual(is_int, True)

    def test_IsPositiveInt(self):

        #Passing direcitly integers because this IsPositiveInt() method
        #is called after converting into int, inside the game

        self.PlayerInputValidator.choosen_column = -10
        is_positive_int = self.PlayerInputValidator.IsPositiveInt()

        self.assertEqual(is_positive_int, False)


        self.PlayerInputValidator.choosen_column = 10
        is_positive_int = self.PlayerInputValidator.IsPositiveInt()

        self.assertEqual(is_positive_int, True)



    def test_IsChoosenColumnInBound(self):
        self.PlayerInputValidator.choosen_column = -1
        is_column_in_bound = self.PlayerInputValidator.IsChoosenColumnInBound()

        self.assertEqual(is_column_in_bound, False)


        self.PlayerInputValidator.choosen_column = 10
        is_column_in_bound = self.PlayerInputValidator.IsChoosenColumnInBound()

        self.assertEqual(is_column_in_bound, False)


        self.PlayerInputValidator.choosen_column = 4
        is_column_in_bound = self.PlayerInputValidator.IsChoosenColumnInBound()

        self.assertEqual(is_column_in_bound, True)


        self.PlayerInputValidator.choosen_column = 7
        is_column_in_bound = self.PlayerInputValidator.IsChoosenColumnInBound()

        self.assertEqual(is_column_in_bound, True)


        self.PlayerInputValidator.choosen_column = 1
        is_column_in_bound = self.PlayerInputValidator.IsChoosenColumnInBound()

        self.assertEqual(is_column_in_bound, True)