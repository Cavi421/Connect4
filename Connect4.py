from Player.AI import AIClass
from Player.Human import HumanClass
from Board.Board import BoardClass


class Connect4Class():

    def __init__(self : object) -> None:
        
        self.player1 = AIClass(1)
        self.player2 = AIClass(2)

        self.game_ended = False

    def IsGameWon(self, Board: BoardClass):
        pass


    def IsGameDraw(self, Board: BoardClass) -> bool:
        #Check there are no zeroes on the upmost row

         
         if not 0 in Board.matrix_board:
             print("DRAW!")

             return True


    def StartGame(self: object) -> None:

        self.Board = BoardClass()


        while not self.game_ended:

            #Phase1
            choosen_column = self.player1.ThinkMove(self.Board)

            #if self.CheckWinningCondition(self.Board.matrix_board):
            #    self.game_ended = True
            #    break

            #self.CheckDraw()
            self.Board.AddToken(choosen_column, self.player1)
            self.Board.UpdateBoard()


            #-------------------------------------


            #Phase 2
            choosen_move = self.player2.ThinkMove(self.Board)
            self.Board.AddToken(choosen_move, self.player2)
            #if self.CheckWinningCondition(self.Board.matrix_board):
            #    self.game_ended = True
            #    break


            #self.CheckDraw()
            self.Board.UpdateBoard()


            if self.IsGameDraw(self.Board):
                break




