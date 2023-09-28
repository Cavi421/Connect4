from Player.AI import AIClass
from Player.Human import HumanClass
from Board.Board import BoardClass
from Referee.Referee import RefereeClass
from random import randint


class Connect4Class:
    """
    Main class that handles:
    -Randomize the turns
    -Turns between the players
    -Instantiates the players
    """

    def __init__(self: object) -> None:
        # Randomize who goes first
        if randint(1, 2) == 1:
            self.player1 = HumanClass(1)
            self.player2 = AIClass(2)
        else:
            self.player1 = AIClass(1)
            self.player2 = HumanClass(2)

        #set game ended as false for the while loop
        self.game_ended = False

    def StartGame(self: object) -> None:

        #Instantiates needed classes
        self.Board = BoardClass()
        self.Board.UpdateBoard()
        self.Referee = RefereeClass()

        while not self.game_ended:

            # -------------------------------------
            # PLAYER 1 TURN
            # -------------------------------------
            print("-------------------------------------\n")

            #Get player input
            choosen_column = self.player1.ThinkMove(self.Board)

            #Add token to the board
            last_move = self.Board.AddToken(choosen_column, self.player1)

            #Refresh board
            self.Board.UpdateBoard()
            # print(last_move)

            #Check win conditions
            if self.Referee.IsGameWon(self.Board, last_move, self.player1):
                self.Board.UpdateBoard()
                break

            print("-------------------------------------\n")

            # -------------------------------------
            # PLAYER 2 TURN
            # -------------------------------------
            #Get player input
            choosen_move = self.player2.ThinkMove(self.Board)

            #Add token to the board
            last_move = self.Board.AddToken(choosen_move, self.player2)

            #refresh board
            self.Board.UpdateBoard()

            #Check win conditions
            if self.Referee.IsGameWon(self.Board, last_move, self.player2):
                self.Board.UpdateBoard()
                break

            # -------------------------------------

            #Check if the game is a draw
            if self.Referee.IsGameDraw(self.Board):
                self.Board.UpdateBoard()
                break
