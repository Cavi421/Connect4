from Board.Board import BoardClass
from Validator.Validator import ValidatorClass


class PlayerInputValidatorClass(ValidatorClass):
    """
    This class will perform a serious of checks
    to validate:
    -if the value inserted by the player is of the correct type(int)
    -Check if the move can be done
    """

    def CheckInput(self, player_input: int) -> bool:
        if not self.IsEmpty(player_input):
            return False
        if not self.IsInt(player_input):
            return False

        # After IsInt check, column is stored as INT type to avoid converting from string it each time
        if not self.IsPositiveInt(player_input):
            return False
        if not self.IsChoosenColumnInBound(player_input):
            return False

        return True

    def IsEmpty(self, choosen_column: int) -> bool:
        if choosen_column == "":
            print("Choose value is empty, try again")
            return False

        else:
            return True

    def IsInt(self, choosen_column: int) -> bool:
        try:
            self.choosen_column = int(choosen_column)
            return True

        except Exception as e:
            print(e)
            print("Input choosen is not a number, try again")
            return False

    def IsPositiveInt(self, choosen_column: int) -> bool:
        if self.choosen_column < 0:
            print("Column Number is negative, try again")
            return False

        else:
            return True

    def IsChoosenColumnInBound(self, choosen_column: int) -> bool:
        if self.choosen_column <= 0 or self.choosen_column >= 8:
            print("Wrong column number. Column should be between 1 and 7")
            return False

        else:
            return True
