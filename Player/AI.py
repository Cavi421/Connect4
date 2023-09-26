from Player.Player import PlayerClass
from Board.Board import BoardClass
from random import randint

class AIClass(PlayerClass):


    def ThinkMove(self, Board: BoardClass) -> int:

        random_column = self.AICalculateRandomPositionToAddToken(Board)

        return random_column

    

    def AICalculateRandomPositionToAddToken(self, Board: BoardClass ) -> int:
        random_column = randint(0,6)
        
        return random_column