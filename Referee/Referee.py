from Board.Board import BoardClass


class RefereeClass:
    def __init__(self):
        pass

    def HorizontalCheckWin(
        self, Board: BoardClass, last_move: tuple, player: object
    ) -> bool:
        """
        The algo to check the win condition works like this:
        Given the last move, it'll check on the left and on the right additional tokens
        beloging to the same player using 2 for loops one for left and one for right.
        If it finds a token who is from a different player then it'll stop searching on that direction.
        Win condition is achieved when it finds at least 4 connected tokens.
        """

        row_last_move, column_last_move = last_move

        # List used to contain the values of player ids (it'll contain 1 or 2)
        # It doesn't start empty because in this way we can skip a loop iteration
        # for the first element which is the last_move token and it's always counted
        board_values_to_check = [player.id]
        cells_to_convert_in_winning_line = [last_move]
    

        # Right loop
        # column_last_move +1 because in this way we exclude the first element which is the
        # last_move_token
        for number_of_right_scans, r_offset in enumerate(
            range(column_last_move + 1, 7)
        ):
            # If finds another token then it stops scanning
            if Board.matrix_board[row_last_move][r_offset] != player.id:
                break

            # The algo checks max 3 position away from last_move position
            # number_of_scans is the current for loop iteration number
            if number_of_right_scans >= 3:
                break

            board_values_to_check.append(Board.matrix_board[row_last_move][r_offset])
            cells_to_convert_in_winning_line.append(
                (row_last_move, r_offset)
            )

        # Left loop same as above
        for number_of_left_scans, l_offset in enumerate(
            range(column_last_move - 1, -1, -1)
        ):
            if Board.matrix_board[row_last_move][l_offset] != player.id:
                break

            if number_of_left_scans >= 3:
                break

            board_values_to_check.append(Board.matrix_board[row_last_move][l_offset])

            cells_to_convert_in_winning_line.append(
                (row_last_move, l_offset)
            )

        # If it finds more than 4 connected tokens then it's a win
        # Connection is ensured on the above checks
        if len((board_values_to_check)) >= 4:
            self.ConvertCellsIntoWinningLine(Board, cells_to_convert_in_winning_line)
            return True

        else:
            False

    def VerticalCheckWin(
        self, Board: BoardClass, last_move: tuple, player: object
    ) -> bool:
        """
        The algo to check the win condition works like this:
        Given the last move, it'll check on the left and on the right additional tokens
        beloging to the same player using 2 for loops one for left and one for right.
        If it finds a token who is from a different player then it'll stop searching on that direction.
        Win condition is achieved when it finds at least 4 connected tokens.
        """

        row_last_move, column_last_move = last_move

        board_values_to_check = [player.id]
        cells_to_convert_in_winning_line = [last_move]

        # Lower scans
        for number_of_lower_scans, lower_offset in enumerate(
            range(row_last_move + 1, 6)
        ):
            # If finds another token then it stops scanning
            if Board.matrix_board[lower_offset][column_last_move] != player.id:
                break

            # The algo checks max 3 position away from last_move position
            # number_of_scans is the current for loop iteration number
            if number_of_lower_scans >= 3:
                break

            board_values_to_check.append(
                Board.matrix_board[lower_offset][column_last_move]
            )

            cells_to_convert_in_winning_line.append(
                (lower_offset, column_last_move)
            )

        # Upper scans
        for number_of_upper_scans, u_offset in enumerate(
            range(row_last_move - 1, -1, -1)
        ):
            # If finds another token then it stops scanning
            if Board.matrix_board[u_offset][column_last_move] != player.id:
                break

            # The algo checks max 3 position away from last_move position
            # number_of_scans is the current for loop iteration number
            if number_of_upper_scans >= 3:
                break

            board_values_to_check.append(Board.matrix_board[u_offset][column_last_move])

            cells_to_convert_in_winning_line.append(
                (u_offset, column_last_move)
            )

        # print(Board.matrix_board[row_last_move][column_last_move], f"(r:{row_last_move}, c:{column_last_move})")
        # print(cells_to_convert_in_winning_line)

        if len((board_values_to_check)) >= 4:
            self.ConvertCellsIntoWinningLine(Board, cells_to_convert_in_winning_line)
            return True

        else:
            False

        # Down Scans

    # \
    def DiagonalCheckLeft(
        self, Board: BoardClass, last_move: tuple, player: object
    ) -> bool:
        row_last_move, column_last_move = last_move
        board_values_to_check = [player.id]
        cells_to_convert_in_winning_line = [last_move]

        # Lower RIGHT scans
        for number_of_lower_right_scans, lower_offset in enumerate(
            range(row_last_move + 1, 6)
        ):
            right_offset = number_of_lower_right_scans + 1

            column_last_move_plus_right_offset = column_last_move + right_offset

            # outbound check for right offset
            # If reached outbound limit then stop scanning
            max_column_id = 6
            if (column_last_move_plus_right_offset) > max_column_id:
                break

            if (
                Board.matrix_board[lower_offset][column_last_move_plus_right_offset]
                != player.id
            ):
                break

            if number_of_lower_right_scans >= 3:
                break

            board_values_to_check.append(
                Board.matrix_board[lower_offset][column_last_move_plus_right_offset]
            )
            cells_to_convert_in_winning_line.append((lower_offset, column_last_move_plus_right_offset))

        # Upper Left Scans
        # Needs to reach the 0th row, so it's going backwards until -1 excluded
        for number_of_upper_left_scans, upper_offset in enumerate(
            range(row_last_move - 1, -1, -1)
        ):
            left_offset = number_of_upper_left_scans + 1

            # Negative because it needs to go to the left
            column_last_move_minus_left_offset = column_last_move - left_offset

            # Outbound left check
            min_column_id = 0
            if (column_last_move_minus_left_offset) < min_column_id:
                break

            if (
                Board.matrix_board[upper_offset][column_last_move_minus_left_offset]
                != player.id
            ):
                break

            if number_of_upper_left_scans >= 3:
                break

            board_values_to_check.append(
                Board.matrix_board[upper_offset][column_last_move_minus_left_offset]
            )
            cells_to_convert_in_winning_line.append(
                (upper_offset, column_last_move_minus_left_offset)
            )

        # print(Board.matrix_board[row_last_move][column_last_move], f"(r:{row_last_move}, c:{column_last_move})")
        # print(cells_to_convert_in_winning_line)

        if len((board_values_to_check)) >= 4:
            self.ConvertCellsIntoWinningLine(Board, cells_to_convert_in_winning_line)
            return True

        else:
            False

    # /
    def DiagonalCheckRight(
        self, Board: BoardClass, last_move: tuple, player: object
    ) -> bool:
        row_last_move, column_last_move = last_move
        board_values_to_check = [player.id]
        cells_to_convert_in_winning_line = [last_move]

        # Lower LEFT scans
        for number_of_lower_left_scans, lower_offset in enumerate(
            range(row_last_move + 1, 6)
        ):
            left_offset = number_of_lower_left_scans + 1

            column_last_move_minus_left_offset = column_last_move - left_offset

            min_column_id = 0
            if (column_last_move_minus_left_offset) < min_column_id:
                break

            if (
                Board.matrix_board[lower_offset][column_last_move_minus_left_offset]
                != player.id
            ):
                break

            if number_of_lower_left_scans >= 3:
                break

            board_values_to_check.append(
                Board.matrix_board[lower_offset][column_last_move_minus_left_offset]
            )

            cells_to_convert_in_winning_line.append(
                (lower_offset, column_last_move_minus_left_offset)
            )

        # UPPER RIGHT SCANS
        for number_of_upper_right_scans, upper_offset in enumerate(
            range(row_last_move - 1, -1, -1)
        ):
            right_offset = number_of_upper_right_scans + 1

            column_last_move_plus_right_offset = column_last_move + right_offset

            # Outbound Right Check
            max_column_id = 6
            if (column_last_move_plus_right_offset) > max_column_id:
                break

            if (
                Board.matrix_board[upper_offset][column_last_move_plus_right_offset]
                != player.id
            ):
                break

            if number_of_upper_right_scans >= 3:
                break

            board_values_to_check.append(
                Board.matrix_board[upper_offset][column_last_move_plus_right_offset]
            )

            cells_to_convert_in_winning_line.append(
                (upper_offset, column_last_move_plus_right_offset)
            )

        # print(Board.matrix_board[row_last_move][column_last_move], f"(r:{row_last_move}, c:{column_last_move})")
        # print(debug_cells_to_check)

        if len((board_values_to_check)) >= 4:
            self.ConvertCellsIntoWinningLine(Board, cells_to_convert_in_winning_line)
            return True

        else:
            False

    def ConvertCellsIntoWinningLine(
        self, Board: BoardClass, cells_to_convert_in_winning_line: list[tuple]
    ) -> None:
        for cell in cells_to_convert_in_winning_line:
            row_id, column_id = cell
            Board.matrix_board[row_id][column_id] = 3

    def IsGameWon(self, Board: BoardClass, last_move: tuple, player: object) -> bool:
        """
        Method to check the various win conditions
        """

        if self.HorizontalCheckWin(Board, last_move, player):
            print(f"Player {player.id} won: HORIZONTAL WIN")
            return True

        if self.VerticalCheckWin(Board, last_move, player):
            print(f"Player {player.id} won: VERTICAL WIN")
            return True

        if self.DiagonalCheckLeft(Board, last_move, player):
            print(f"Player {player.id} won: LEFT DIAGONAL")
            return True

        if self.DiagonalCheckRight(Board, last_move, player):
            print(f"Player {player.id} won: RIGHT DIAGONAL")
            return True

        return False

    def IsGameDraw(self, Board: BoardClass) -> bool:
        """
        Method used to check if a match is draw
        Check if there are no zeroes in the upmost row
        """

        if not 0 in Board.matrix_board[0]:
            print("DRAW!")

            return True