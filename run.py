import time
from Connect4 import Connect4Class


run_tests = False


if __name__ == "__main__":

    if run_tests == True:
        pass

    
    while True:

        if run_tests == False:
            Connect4 = Connect4Class()
            Connect4.StartGame()
        time.sleep(0.1)
