from Player.Player import PlayerClass
from Board.Board import BoardClass
from Validator.PlayerInputValidator import PlayerInputValidatorClass
from Validator.MoveValidator import MoveValidatorClass


class HumanClass(PlayerClass):

    def SetName(self):
        self.name = f"Player n{self.id}"
        self.isAI = False



    def ThinkMove(self, Board: BoardClass) -> int:


        PlayerInputValidator = PlayerInputValidatorClass()

        is_input_correct = False
        is_move_correct = False


        while not is_input_correct or not is_move_correct:
            self.choosen_column = input("SELECT a column number where to place the Token: ")

            is_input_correct = PlayerInputValidator.CheckInput(self.choosen_column)


            if not is_input_correct:
                continue


            #Converted column, taken directly from the validator object
            #self.choosen_column = PlayerInputValidator.choosen_column
            self.choosen_column = int(self.choosen_column)

            # This is to facilitate users, numbering the columns from 1 to 7
            # In reality matrices work with indices from 0 to 6
            # So this line is to convert from a human-readable index to the matrix's one
            self.choosen_column -= 1


            #### VALIDATE IF A MOVE IS CORRECT using Validator ####
            MoveValidator = MoveValidatorClass()
            is_move_correct = MoveValidator.CheckMove(self.choosen_column , Board, self)


        return self.choosen_column



