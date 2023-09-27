from Player.Player import PlayerClass
from Board.Board import BoardClass
from Validator.MoveValidator import MoveValidatorClass
from random import randint

class AIClass(PlayerClass):


    def SetName(self):
        self.name = f"AI n{self.id}"
        self.isAI = True


    def ThinkMove(self, Board: BoardClass) -> int:

        random_column = self.AICalculateRandomPositionToAddToken(Board)

        return random_column

    

    def AICalculateRandomPositionToAddToken(self, Board: BoardClass ) -> int:

        MoveValidator = MoveValidatorClass()

        is_move_valid = False
        while not is_move_valid:

            random_column = randint(0,6)

            is_move_valid =  MoveValidator.CheckMove(random_column, Board, self)

        return random_column