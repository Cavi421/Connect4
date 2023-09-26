from Board.Board import BoardClass
from Validator.Validator import ValidatorClass
from Utility.Utility import UtilityClass

class MoveValidatorClass(ValidatorClass):
    """
    This class will perform a serious of checks
    to validate:
    -if the value inserted by the player is of the correct type(int)
    -Check if the move can be done
    """

    def CheckMove(self, column_choosen: int, Board: BoardClass) -> bool:
        

        if not self.CheckIfColumnIsNotFull(column_choosen, Board): 
            print("This column is full, try another one")
            return False



    def CheckIfColumnIsNotFull(self, column_choosen, Board: BoardClass) -> bool:

        Utility = UtilityClass()

        if Utility.ScanMatrixColumnToSeeIfIsNotFull(column_choosen, Board) == False:
            print("Couldn't place token here, column is already full. Choose another column")
            return False
        
        return True
            