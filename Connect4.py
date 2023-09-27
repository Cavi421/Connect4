from Player.AI import AIClass
from Player.Human import HumanClass
from Board.Board import BoardClass


class Connect4Class():

    def __init__(self : object) -> None:
        
        self.player1 = AIClass(1)
        self.player2 = AIClass(2)

        self.game_ended = False


    def HorizontalCheckWin(self, Board: BoardClass, last_move: tuple, player: object) -> bool:

        row_last_move, column_last_move = last_move
        print(Board.matrix_board[row_last_move][column_last_move], f"(r:{row_last_move}, c:{column_last_move})")

        board_values_to_check = [player.id]
        debug_cells_to_check = [(row_last_move, column_last_move)]

        #Based on the last_move position we need to check only 
        #A on the right  column_last_move = column_last_move = 
        #B on the left column_last_move = range()
        for i,r in enumerate(range(column_last_move + 1, 7)):
            

            if Board.matrix_board[row_last_move][r] != player.id:
                break

            if i >= 3:
                break

            #print(f"R to check: {row_last_move}, {r}, board_value:{Board.matrix_board[row_last_move][column_last_move]}, player_id: {player.id}")


            board_values_to_check.append(Board.matrix_board[row_last_move][r])
            debug_cells_to_check.append(([row_last_move],[r]))



        for j,l in enumerate(range(column_last_move -1, -1, -1)):

            if Board.matrix_board[row_last_move][l] != player.id:
                break

            if j >= 3:
                break

            #print(f"L to check: {row_last_move}, {l}")
            board_values_to_check.append(Board.matrix_board[row_last_move][l])
            debug_cells_to_check.append((row_last_move,l))




        print(board_values_to_check)
        print(debug_cells_to_check)

        if len((board_values_to_check)) >= 4 :
            return True
        
        else:
            False



    def IsGameWon(self, Board: BoardClass, last_move: tuple, player: object) -> bool:
        
        
        if self.HorizontalCheckWin(Board, last_move, player):
            return True

        

        return False
        





    def IsGameDraw(self, Board: BoardClass) -> bool:
        """Check there are no zeroes on the upmost row"""
    
        if not 0 in Board.matrix_board[0]:
            print("DRAW!")

            return True


    def StartGame(self: object) -> None:

        self.Board = BoardClass()


        while not self.game_ended:

            #Phase1
            choosen_column = self.player1.ThinkMove(self.Board)


            last_move = self.Board.AddToken(choosen_column, self.player1)
            self.Board.UpdateBoard()
            #print(last_move)


            
            if self.IsGameWon(self.Board, last_move, self.player1):
                print(f"{self.player1.name} WON")
                break


            #-------------------------------------


            #Phase 2
            choosen_move = self.player2.ThinkMove(self.Board)
            last_move = self.Board.AddToken(choosen_move, self.player2)
            self.Board.UpdateBoard()


            if self.IsGameWon(self.Board, last_move, self.player2):
                print(f"{self.player2.name} WON")
                break



            if self.IsGameDraw(self.Board):
                print(f"{self.player1.name} vs {self.player2.name}")
                break




