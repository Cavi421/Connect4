from Player.AI import AIClass
from Player.Human import HumanClass
from Board.Board import BoardClass
from Referee.Referee import RefereeClass
from random import randint


class Connect4Class:
    def __init__(self: object) -> None:
        # Randomize who goes first
        if randint(1, 2) == 1:
            self.player1 = HumanClass(1)
            self.player2 = AIClass(2)
        else:
            self.player1 = AIClass(1)
            self.player2 = HumanClass(2)

        self.game_ended = False

    def StartGame(self: object) -> None:
        self.Board = BoardClass()
        self.Board.UpdateBoard()


        self.Referee = RefereeClass()

        while not self.game_ended:
            # -------------------------------------
            # PLAYER 1 TURN
            print("-------------------------------------\n")
            choosen_column = self.player1.ThinkMove(self.Board)

            last_move = self.Board.AddToken(choosen_column, self.player1)
            self.Board.UpdateBoard()
            # print(last_move)

            if self.Referee.IsGameWon(self.Board, last_move, self.player1):
                self.Board.UpdateBoard()
                break

            print("-------------------------------------\n")

            # -------------------------------------
            # PLAYER 2 TURN
            choosen_move = self.player2.ThinkMove(self.Board)
            last_move = self.Board.AddToken(choosen_move, self.player2)
            self.Board.UpdateBoard()

            if self.Referee.IsGameWon(self.Board, last_move, self.player2):
                self.Board.UpdateBoard()
                break

            # -------------------------------------

            if self.Referee.IsGameDraw(self.Board):
                self.Board.UpdateBoard()
                break
