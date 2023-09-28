import unittest
from Board.Board import BoardClass
from Referee.Referee import RefereeClass
from Player.Human import HumanClass


class TestValidator(unittest.TestCase):
    # This method gets called before starting every test
    # It creates the board
    def setUp(self: object) -> None:
        self.Board = BoardClass()
        self.player1 = HumanClass(1)
        self.Referee = RefereeClass()

    # Testing if a move is correct
    # Player's inputs are converted into strings automatically by input()

    def test_HorizontalCheckWin_3Tokens(self: object) -> None:
        # Fill the first row with 3 tokens
        for i in range(0, 3):
            last_move = self.Board.AddToken(i, self.player1)

        # self.Board.UpdateBoard()

        # Since there are only 3 tokens, it'll take the last one added and use it as last_move
        # with 3 tokens it's impossible to win so it should return False
        is_horizontal_check_win = self.Referee.HorizontalCheckWin(
            self.Board, last_move, self.player1
        )

        # Since there are only 3 tokens,
        self.assertEqual(is_horizontal_check_win, False)

    def test_HorizontalCheckWin_4TokensLeft(self: object) -> None:
        # Fill the first row with 3 tokens
        for i in range(0, 4):
            last_move = self.Board.AddToken(i, self.player1)

        # self.Board.UpdateBoard()

        # it'll take the last one added and use it as last_move
        # With 4 tokens on the same line it should return True since it's considered a win condition
        is_horizontal_check_win = self.Referee.HorizontalCheckWin(
            self.Board, last_move, self.player1
        )

        # Since there are only 3 tokens,
        self.assertEqual(is_horizontal_check_win, True)

    def test_HorizontalCheckWin_4TokensRight(self: object) -> None:
        # Fill the first row with 4 tokens from right to left
        for i in range(6, 2, -1):
            last_move = self.Board.AddToken(i, self.player1)

        # self.Board.UpdateBoard()

        # it'll take the last one added and use it as last_move
        # With 4 tokens on the same line it should return True since it's considered a win condition
        is_horizontal_check_win = self.Referee.HorizontalCheckWin(
            self.Board, last_move, self.player1
        )

        # Since there are only 3 tokens,
        self.assertEqual(is_horizontal_check_win, True)

    def test_VerticalCheckWin_3Tokens(self: object) -> None:
        # Fill the first column with 3 tokens
        for i in range(0, 3):
            last_move = self.Board.AddToken(0, self.player1)

        # self.Board.UpdateBoard()

        # it'll take the last one added and use it as last_move
        # With 3 tokens on the same line it should return False
        is_vertical_check_win = self.Referee.VerticalCheckWin(
            self.Board, last_move, self.player1
        )

        # Since there are only 3 tokens,
        self.assertEqual(is_vertical_check_win, False)

    def test_VerticalCheckWin_4Tokens(self: object) -> None:
        # Fill the first column with 4 tokens
        for i in range(0, 4):
            last_move = self.Board.AddToken(0, self.player1)

        # self.Board.UpdateBoard()

        # it'll take the last one added and use it as last_move
        # With 4 tokens on the same line it should return True since it's considered a win condition
        is_vertical_check_win = self.Referee.VerticalCheckWin(
            self.Board, last_move, self.player1
        )

        self.assertEqual(is_vertical_check_win, True)

    def test_DiagonalCheckLeftWin_RightLoop(self: object) -> None:
        # Fill the first 3 rows and then add another token to trigger the win condition
        for j in range(0, 3):
            for i in range(0, 7):
                self.Board.AddToken(i, self.player1)

        # Add token on first column creating a diagonal left win condition
        last_move = self.Board.AddToken(0, self.player1)

        is_diagonal_left_win = self.Referee.DiagonalCheckLeftWin(
            self.Board, last_move, self.player1
        )

        self.assertEqual(is_diagonal_left_win, True)

    def test_DiagonalCheckLeftWin_LeftLoop(self: object) -> None:
        # create a matrix where to insert the last token, triggering a Diagonal Check Left win condition
        # testing left loop
        for j in range(0, 4):
            for i in range(0, 7):
                # Skip adding tokens on 4th column
                if i == 3:
                    continue

                self.Board.AddToken(i, self.player1)

        # Add token on first column creating a diagonal left win condition
        last_move = self.Board.AddToken(3, self.player1)

        # self.Board.UpdateBoard()

        is_diagonal_left_win = self.Referee.DiagonalCheckLeftWin(
            self.Board, last_move, self.player1
        )
        self.assertEqual(is_diagonal_left_win, True)

    def test_DiagonalCheckRightWin_LeftLoop(self: object) -> None:
        # Fill the first 3 rows and then add another token to trigger the win condition
        for j in range(0, 3):
            for i in range(0, 7):
                self.Board.AddToken(i, self.player1)

        # Add token on last column creating a diagonal right win condition
        last_move = self.Board.AddToken(6, self.player1)

        is_diagonal_right_win = self.Referee.DiagonalCheckRightWin(
            self.Board, last_move, self.player1
        )

        self.assertEqual(is_diagonal_right_win, True)

    def test_DiagonalCheckRightWin_RightLoop(self: object) -> None:

        # create a matrix where to insert the last token, triggering a Diagonal Check Right win condition
        # testing left loop
        for j in range(0, 4):
            for i in range(0, 7):
                # Skip adding tokens on 4th column
                if i == 3:
                    continue

                self.Board.AddToken(i, self.player1)

        # Add token on first column creating a diagonal right win condition
        last_move = self.Board.AddToken(3, self.player1)

        #self.Board.UpdateBoard()

        is_diagonal_right_win = self.Referee.DiagonalCheckRightWin(
            self.Board, last_move, self.player1
        )
        self.assertEqual(is_diagonal_right_win, True)
