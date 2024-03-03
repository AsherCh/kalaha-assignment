from Board import *

def print_board(board):
    state = board.get_state()
    print ("-------------Kalaha----------------")
    print ("-------------By Group 39-----------")

    print ("You will play this game with the computer.Please pick up your stones from your side first")
    print("==========================================")
    print("Computer", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[0][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("        ", end=" ");print("|", end=" "); print(state[0][-1],end=" ");print("|",end="");print("----------------------",end="");print(" |",end=" ");print(state[1][-1],end=" ");print("|")
    print("   Human", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[1][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("==========================================")

if __name__ == "__main__":
    # Play the game
    HUMAN_PLAYER = 0
    COMPUTER_PLAYER = 1
    board = Board()
    print_board (board)
    print ("Please pick up your stones from your side:")
    pit_index = int(input())-1
    board.take_stones(pit_index)
