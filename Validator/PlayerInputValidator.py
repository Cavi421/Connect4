from Board.Board import BoardClass
from Validator.Validator import ValidatorClass


class PlayerInputValidatorClass(ValidatorClass):
    """
    This class will perform a series of sanity checks to make sure
    that the human's player input is an INT between 1 and 7
    If not returns False and the method which called this one
    will keep looping.
    """

    def CheckInput(self, player_input: int) -> bool:
        self.choosen_column = player_input

        if not self.IsEmpty():
            return False
        if not self.IsInt():
            return False
        if not self.IsPositiveInt():
            return False
        if not self.IsChoosenColumnInBound():
            return False

        #If all the checks pass then return True
        return True

    def IsEmpty(self) -> bool:
        if self.choosen_column == "":
            print("Warning: Choose value is empty, try again")
            return False

        else:
            return True

    def IsInt(self) -> bool:
        try:
            self.choosen_column = int(self.choosen_column)
            return True

        except ValueError as e:
            #print(e)
            print("Warning: Input choosen is not an Integer number, try again")
            return False

    def IsPositiveInt(self) -> bool:
        if self.choosen_column < 0:
            print("Warning: Column number can't be negative, try again")
            return False

        else:
            return True

    def IsChoosenColumnInBound(self) -> bool:
        if self.choosen_column <= 0 or self.choosen_column >= 8:
            print("Warning: Wrong column number,it should be between 1 and 7")
            return False

        else:
            return True
