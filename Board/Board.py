# import numpy as np
from Player.Player import PlayerClass
from Utility.Utility import UtilityClass


class BoardClass:
    def __init__(self: object) -> None:
        # Generate the 6x7 matrix using nested list comprehension
        # instead of hard coding it
        self.matrix_board = [[0 for i in range(0, 7)] for j in range(0, 6)]
        self.UpdateBoard()

    def UpdateBoard(self: object) -> None:
        """
        Convert the self.board matrix into a human-readable format using strings and print
        """

        converted_board = ""

        converted_board += "--|  1  |  2  |  3  |  4  |  5  |  6  |  7  |\n"

        for row_index, row in enumerate(self.matrix_board):
            converted_board += (
                f"---------------------------------------------\n{row_index} |  "
            )

            for column_index, column_value in enumerate(row):
                if column_value == 0:
                    converted_board += "   |  "

                elif column_value == 1:
                    converted_board += "O  |  "

                elif column_value == 2:
                    converted_board += "X  |  "

                elif column_value == 3:
                    converted_board += "!! |  "

                if column_index == 6:
                    converted_board += "\n"

        print(converted_board)

    def AddToken(self: object, choosen_column: int, player: PlayerClass) -> tuple:
        """
        Add a token inside the matrix.
        Determine the appropriate placement for the token.
        Return the coordinates in a tuple.
        """

        empty_position_row_id = self.ComputeTokenPosition(choosen_column)

        self.matrix_board[empty_position_row_id][choosen_column] = player.id

        # Return the token coordinates inside the matrix. ex. (1,2) mean row index 1 and column index 2
        return (empty_position_row_id, choosen_column)

    def ComputeTokenPosition(self: object, choosen_column: int):
        """
        When adding a token this function check where is the correct position in the matrix
        to place the token(it can't float around, it needs to have another token below or being at row 0)
        """
        Utility = UtilityClass()

        empty_position_row_id = Utility.ScanMatrixColumnForEmptyPositionId(
            choosen_column, self
        )

        # Insert additional checks here

        return empty_position_row_id
