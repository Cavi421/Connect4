from Board.Board import BoardClass
from Validator.Validator import ValidatorClass
from Utility.Utility import UtilityClass
from Player.Player import PlayerClass

class MoveValidatorClass(ValidatorClass):
    """
    This class will perform a serious of checks
    to validate:
    -if the value inserted by the player is of the correct type(int)
    -Check if the move can be done
    """

    def CheckMove(self, column_choosen: int, Board: BoardClass, player: PlayerClass) -> bool:
        

        if not self.CheckIfColumnIsNotFull(column_choosen, Board):

            if not player.isAI:
                print("Warning: This column is full, try again")
                
            return False
        
        
        return True



    def CheckIfColumnIsNotFull(self, column_choosen, Board: BoardClass) -> bool:

        Utility = UtilityClass()

        if Utility.ScanMatrixColumnToSeeIfIsNotFull(column_choosen, Board) == False:
            return False
        
        return True
            