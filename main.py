from Board import *

def print_board(board):
    state = board.get_state()

    print("==========================================")
    print("Computer", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[0][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("        ", end=" ");print("|", end=" "); print(state[0][-1],end=" ");print("|",end="");print("----------------------",end="");print(" |",end=" ");print(state[1][-1],end=" ");print("|")
    print("   Human", end=" ");print("|", end="  "); print(" |",end=" ");print(*state[1][0:-1],sep=" | ",end="");print(" |",end="  ");print(" |")
    print("==========================================")

if __name__ == "__main__":
    print ("-------------Kalaha----------------")
    print ("-------------By Group 39-----------")
    print ("You will play this game with the computer.Please pick up your stones from your side first")
    # Play the game
    HUMAN = 1
    COMPUTER = 0
    MAX_DEPTH = 2
    #Human as the first player
    board = Board(HUMAN)
    #print the initial board
    print_board (board)
    #Set the board status as the node
    index =0
    while index < 7:
        #Human input the first move
        current_player=board.get_turn()
        print (current_player," Human,please pick up your stones from your side:")
        pit_index = int(input())-1
        board.take_stones(pit_index)
        print_board (board)
        #Change the player to the computer
        board.reverse_player()
        current_player=board.get_turn()
        print (current_player," Computer's best move")
        root_node = Node(board)
        tree = Tree(root_node,MAX_DEPTH)
        tree.build(tree.get_root(),0)

        print ("                    ")
        print("==========================================")
        #Change the player to the Human
        board.reverse_player()
        index +=1

    print ("Game is over")
